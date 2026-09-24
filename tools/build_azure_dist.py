# -*- coding: utf-8 -*-
"""Assemble the Azure Static Web Apps payloads for the Copilot Multi-Industry Demo Hub.

dist/main  -> hub (index.html, hub.html, data.js, files/), every card site under
              sites/<repo>/, and Diamond/Caldova tenant pages under tenants/<tenant>/.
dist/media -> card sites too large for the main app's 250 MB Free-plan limit.

Card sites come from the public GitHub repos (shallow clones cached outside the
repo), overlaid with newer local copies where configured. Links to the old
steffiyappy.github.io addresses are rewritten to the Azure hosts.

Usage: python tools/build_azure_dist.py
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime
from pathlib import Path

MAIN_HOST = 'https://mango-flower-017ffa400.1.azurestaticapps.net'
MEDIA_HOST = 'https://gray-meadow-0e78e0b00.6.azurestaticapps.net'
GH_USER = 'steffiyappy'
HUB_REPO = 'zava-copilot-demo'

REPO = Path(__file__).resolve().parent.parent
DIST = REPO / 'dist'
OUT = {'main': DIST / 'main', 'media': DIST / 'media'}
HOME = Path.home()
CACHE = HOME / 'source' / 'hub-sites-cache'
# Customer folder names, tenant details and exclusions live outside the public
# repo in this local file.
LOCAL_CONFIG = HOME / '.scout' / 'copilot-demo-hub' / 'local-config.json'
_cfg = json.loads(LOCAL_CONFIG.read_text(encoding='utf-8-sig')) if LOCAL_CONFIG.exists() else {}
MAIN_HOST = _cfg.get('azure', {}).get('main_host', MAIN_HOST)
MEDIA_HOST = _cfg.get('azure', {}).get('media_host', MEDIA_HOST)
MATERIALS = HOME / _cfg.get('materials', 'missing-materials-folder')

MEDIA_SITES = {'contoso-mining-services-demo'}
# Newer local copies that replace or extend the GitHub version.
OVERLAYS = {repo: HOME / rel for repo, rel in _cfg.get('overlays', {}).items()}
# Sites that exist only locally: slug -> (folder, files to publish)
LOCAL_SITES = {slug: (HOME / v['folder'], v['files']) for slug, v in _cfg.get('local_sites', {}).items()}
# Tenant email sets whose content names a real organisation stay unpublished.
EMAIL_SETS_EXCLUDED = set(_cfg.get('email_sets_excluded', []))
REAL_NAME_SUFFIXES = tuple(_cfg.get('real_name_suffixes', []))
TENANTS = {k: tuple(v) for k, v in _cfg.get('tenants', {}).items()}
PACKS = {
    'Contoso Gold Mining Co - Copilot Chat': ('contoso-gold-mining-copilot-chat', 'Contoso Gold Mining: Copilot Chat (Basic) pack',
                                              'Full Copilot Chat site with a daily briefing, six exercises and five sample files. Password: ContosoGold2026.'),
    'Nusantara Mineral Terpadu - SharePoint SOP Files': ('nusantara-sop-files', 'Nusantara Mineral Terpadu: SharePoint SOP files',
                                                         'Five IT SOPs to upload to SharePoint for the IT FAQ agent demo.'),
    'Palmaraya Agri - SharePoint SOP Files': ('palmaraya-sop-files', 'Palmaraya Agri: SharePoint SOP files',
                                              'Five safety and operations SOPs to upload to SharePoint for the Operations and Safety Assistant demo.'),
}
SKIP_DIRS = {'.git', '.github', 'node_modules', '__pycache__'}
SKIP_FILES = {'.nojekyll', '.gitattributes', '.gitignore', 'README.md'}
TEXT_EXT = {'.html', '.htm', '.js', '.css', '.json', '.txt', '.md', '.xml', '.svg', '.csv'}
LIMITS = {'main': (245 * 1024 * 1024, 14500), 'media': (245 * 1024 * 1024, 14500)}
report = {'sites': {}, 'rewrites': 0, 'unresolved_links': set(), 'office_files_with_github_links': [], 'overlays': {}}


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f'FAILED: {" ".join(cmd)}\n{r.stderr.strip()}')
    return r.stdout


def card_sites():
    src = (REPO / 'gen_hub.py').read_text(encoding='utf-8')
    block = src[src.index('const OTHER_PAGES = ['):src.index('\n];', src.index('const OTHER_PAGES = ['))]
    return sorted(set(re.findall(r"sites/([A-Za-z0-9_.-]+)/", block)))


def fetch(repo):
    dst = CACHE / repo
    if (dst / '.git').exists():
        run(['git', '-C', str(dst), 'fetch', '--depth', '1', 'origin'])
        run(['git', '-C', str(dst), 'reset', '--hard', 'origin/HEAD'])
    else:
        CACHE.mkdir(parents=True, exist_ok=True)
        run(['git', 'clone', '--depth', '1', '--quiet', f'https://github.com/{GH_USER}/{repo}.git', str(dst)])
    return dst


def copy_tree(src, dst):
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel = Path(root).relative_to(src)
        for f in files:
            if f in SKIP_FILES or f.endswith(('.py', '.pyc')):
                continue
            (dst / rel).mkdir(parents=True, exist_ok=True)
            shutil.copy2(Path(root) / f, dst / rel / f)


def html_refs(path):
    txt = path.read_text(encoding='utf-8', errors='ignore')
    for ref in re.findall(r'''(?:href|src)\s*=\s*["']([^"'#?]+)''', txt):
        if not re.match(r'^(?:[a-z]+:|//|/|\$|\{)', ref, re.I):
            yield ref


def overlay(repo, dst, local, commit_ts):
    """Copy local files that changed after the repo's last commit, plus local
    assets that the site's HTML references but the repo lacks."""
    changed = []
    for f in list(dst.rglob('*')):
        if f.is_file():
            lf = local / f.relative_to(dst)
            if lf.is_file() and lf.stat().st_mtime > commit_ts and lf.read_bytes() != f.read_bytes():
                shutil.copy2(lf, f)
                changed.append(str(f.relative_to(dst)))
    for h in [p for p in dst.rglob('*.html')]:
        for ref in html_refs(h):
            target = (h.parent / ref).resolve()
            if not target.exists():
                lf = (local / h.parent.relative_to(dst) / ref).resolve()
                if lf.is_file() and str(lf).startswith(str(local.resolve())):
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(lf, target)
                    changed.append(str(target.relative_to(dst)) + ' (new)')
    report['overlays'][repo] = changed


def host_for(repo):
    return MEDIA_HOST if repo in MEDIA_SITES else MAIN_HOST


def rewrite_links(root, hosted):
    pat = re.compile(r'https?://' + GH_USER + r'\.github\.io/([A-Za-z0-9_.-]+)/?')

    def sub(m):
        repo = m.group(1)
        if repo == HUB_REPO:
            return MAIN_HOST + '/'
        if repo in hosted:
            return f'{host_for(repo)}/sites/{repo}/'
        report['unresolved_links'].add(repo)
        return m.group(0)

    for f in root.rglob('*'):
        if not f.is_file():
            continue
        if f.suffix.lower() in TEXT_EXT:
            t = f.read_text(encoding='utf-8', errors='surrogateescape')
            nt, n = pat.subn(sub, t)
            if n:
                f.write_text(nt, encoding='utf-8', errors='surrogateescape')
                report['rewrites'] += n
        elif f.suffix.lower() in ('.docx', '.xlsx', '.pptx'):
            try:
                with zipfile.ZipFile(f) as z:
                    if any(GH_USER.encode() + b'.github.io' in z.read(n) for n in z.namelist() if n.endswith('.xml') or n.endswith('.rels')):
                        report['office_files_with_github_links'].append(str(f.relative_to(DIST)))
            except zipfile.BadZipFile:
                pass


def clean_set_name(name):
    for s in REAL_NAME_SUFFIXES:
        name = re.sub(r'\s*-\s*' + re.escape(s) + r'$', '', name)
    return name


def zip_dir(src, dst_zip, arc_root=''):
    with zipfile.ZipFile(dst_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(src.rglob('*.eml')):
            z.write(f, str(Path(arc_root) / f.relative_to(src)))


def build_tenant(slug, label, domain, out):
    base = out / 'tenants' / slug
    base.mkdir(parents=True, exist_ok=True)
    rows_email, rows_pack, all_sets = [], [], []
    email_root = MATERIALS / '01 Email Imports' / label
    for group in ('Current', 'Archived'):
        for d in sorted((email_root / group).iterdir()) if (email_root / group).exists() else []:
            if not d.is_dir() or d.name in EMAIL_SETS_EXCLUDED:
                continue
            name = clean_set_name(d.name)
            n = len([f for f in d.rglob('*.eml')])
            fn = re.sub(r'[^A-Za-z0-9]+', '-', f'{label}-{group}-{name}').strip('-') + '.zip'
            zip_dir(d, base / fn, f'{group}/{name}')
            rows_email.append((group, name, n, fn))
            all_sets.append((d, f'{group}/{name}'))
    all_zip = f'{label}-all-email-imports.zip'
    with zipfile.ZipFile(base / all_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        for d, arc in all_sets:
            for f in sorted(d.rglob('*.eml')):
                z.write(f, str(Path(arc) / f.relative_to(d)))
    pack_root = MATERIALS / '02 Demo Packs' / label
    for folder, (pslug, title, desc) in PACKS.items():
        srcs = sorted((pack_root / folder).glob('source-*')) if (pack_root / folder).exists() else []
        if not srcs:
            continue
        pdst = base / 'packs' / pslug
        copy_tree(srcs[-1], pdst)
        files = sorted(p.name for p in pdst.iterdir() if p.is_file() and p.suffix.lower() in ('.docx', '.zip', '.xlsx', '.pdf'))
        rows_pack.append((pslug, title, desc, (pdst / 'index.html').exists(), files))
    n_emails = sum(r[2] for r in rows_email)
    esc = html.escape
    email_html = ''.join(f'<tr><td>{esc(g)}</td><td>{esc(nm)}</td><td class="n">{n}</td><td><a href="{esc(fn)}" download>Download zip</a></td></tr>' for g, nm, n, fn in rows_email)
    pack_html = ''
    for pslug, title, desc, is_site, files in rows_pack:
        links = [f'<a href="packs/{pslug}/" target="_blank" rel="noopener">Open site</a>'] if is_site else []
        links += [f'<a href="packs/{pslug}/{esc(f)}" download>{esc(f)}</a>' for f in files]
        pack_html += f'<div class="pack"><h3>{esc(title)}</h3><p>{esc(desc)}</p><div class="links">{" ".join(links)}</div></div>'
    stamp = datetime.now().strftime('%d %b %Y, %H:%M')
    page = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,nofollow"><title>{label} tenant demo materials | Copilot Multi-Industry Demo Hub</title>
<script>if(sessionStorage.getItem('hub_auth')!=='ok'){{location.replace('/index.html');}}</script>
<style>
body{{margin:0;font-family:Inter,Segoe UI,system-ui,sans-serif;background:#F0F4F8;color:#1A1A2E}}
header{{background:linear-gradient(135deg,#0F1C3F,#1F2D55 55%,#0078D4);color:#fff;padding:28px 32px}}
header a{{color:#9FE7E7;text-decoration:none;font-size:13px}} h1{{margin:8px 0 4px;font-size:26px}} .sub{{opacity:.8;font-size:14px}}
main{{max-width:1040px;margin:0 auto;padding:24px 20px 48px}} h2{{font-size:18px;margin:28px 0 10px;color:#1F2D55}}
table{{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.08)}}
th,td{{text-align:left;padding:10px 14px;border-bottom:1px solid #E5E7EB;font-size:14px}} th{{background:#F8FAFC;color:#475569;font-weight:600}}
td.n{{text-align:right;font-variant-numeric:tabular-nums}} a{{color:#0078D4;font-weight:600}}
.pack{{background:#fff;border-radius:12px;padding:16px 18px;margin:12px 0;box-shadow:0 1px 3px rgba(0,0,0,.08)}} .pack h3{{margin:0 0 6px;font-size:16px}}
.pack p{{margin:0 0 10px;color:#475569;font-size:14px}} .links a{{display:inline-block;margin:4px 12px 4px 0;font-size:13px}}
.note{{background:#FFF7ED;border:1px solid #FED7AA;border-radius:10px;padding:12px 14px;font-size:13px;color:#7C2D12;margin-top:24px}}
.all{{display:inline-block;margin:6px 0 12px;background:#0078D4;color:#fff;padding:9px 16px;border-radius:8px;text-decoration:none}}
</style></head><body>
<header><a href="/hub.html">&larr; Back to the hub</a><h1>{label} tenant: demo materials</h1>
<div class="sub">Tenant domain: {domain} &middot; {n_emails} import-ready emails &middot; refreshed {stamp}</div></header>
<main>
<h2>Email imports</h2>
<a class="all" href="{all_zip}" download>Download all {n_emails} emails (zip)</a>
<table><thead><tr><th>Group</th><th>Scenario set</th><th>Emails</th><th>File</th></tr></thead><tbody>{email_html}</tbody></table>
<h2>Demo packs</h2>{pack_html}
<div class="note">Tenant guides (one-time setup guide, seller FAQ, chapter narrative) are internal Microsoft documents and are not published on this site.</div>
</main></body></html>'''
    (base / 'index.html').write_text(page, encoding='utf-8')
    report['sites'][f'tenants/{slug}'] = {'emails': n_emails, 'sets': len(rows_email), 'packs': len(rows_pack)}


def write_common(out, kind):
    (out / 'robots.txt').write_text('User-agent: *\nDisallow: /\n', encoding='utf-8')
    cfg = {
        'mimeTypes': {'.eml': 'message/rfc822', '.json': 'application/json', '.md': 'text/markdown; charset=utf-8'},
        'globalHeaders': {'X-Robots-Tag': 'noindex, nofollow'},
        'routes': [{'route': '/data.js', 'headers': {'Cache-Control': 'no-cache'}},
                   {'route': '/hub.html', 'headers': {'Cache-Control': 'no-cache'}},
                   {'route': '/index.html', 'headers': {'Cache-Control': 'no-cache'}}] if kind == 'main' else [],
    }
    (out / 'staticwebapp.config.json').write_text(json.dumps(cfg, indent=2), encoding='utf-8')
    if kind == 'media':
        (out / 'index.html').write_text(f'<!DOCTYPE html><meta charset="UTF-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={MAIN_HOST}/"><title>Copilot Multi-Industry Demo Hub</title><a href="{MAIN_HOST}/">Open the Copilot Multi-Industry Demo Hub</a>', encoding='utf-8')


def measure(out):
    files = [f for f in out.rglob('*') if f.is_file()]
    return sum(f.stat().st_size for f in files), len(files)


def main():
    if not LOCAL_CONFIG.exists():
        sys.exit(f'Local config not found: {LOCAL_CONFIG}')
    for o in OUT.values():
        if o.exists():
            shutil.rmtree(o)
        o.mkdir(parents=True)
    main_out = OUT['main']
    for f in ('index.html', 'hub.html', 'data.js'):
        shutil.copy2(REPO / f, main_out / f)
    copy_tree(REPO / 'files', main_out / 'files')

    sites = card_sites()
    hosted = set(sites) - set(LOCAL_SITES)
    for repo in sorted(hosted):
        src = fetch(repo)
        kind = 'media' if repo in MEDIA_SITES else 'main'
        dst = OUT[kind] / 'sites' / repo
        copy_tree(src, dst)
        if repo in OVERLAYS and OVERLAYS[repo].exists():
            commit_ts = int(run(['git', '-C', str(src), 'log', '-1', '--format=%ct']).strip())
            overlay(repo, dst, OVERLAYS[repo], commit_ts)
        report['sites'][repo] = {'app': kind, 'files': sum(1 for p in dst.rglob('*') if p.is_file())}
        if kind == 'media':
            stub = main_out / 'sites' / repo
            stub.mkdir(parents=True, exist_ok=True)
            (stub / 'index.html').write_text(f'<!DOCTYPE html><meta charset="UTF-8"><meta http-equiv="refresh" content="0; url={MEDIA_HOST}/sites/{repo}/"><a href="{MEDIA_HOST}/sites/{repo}/">Open</a>', encoding='utf-8')
    for slug, (folder, names) in LOCAL_SITES.items():
        dst = main_out / 'sites' / slug
        dst.mkdir(parents=True, exist_ok=True)
        for n in names:
            shutil.copy2(folder / n, dst / n)
        report['sites'][slug] = {'app': 'main', 'files': len(names), 'source': 'local'}

    hub = (main_out / 'hub.html').read_text(encoding='utf-8')
    for repo in MEDIA_SITES:
        hub = hub.replace(f"url: 'sites/{repo}/'", f"url: '{MEDIA_HOST}/sites/{repo}/'")
    (main_out / 'hub.html').write_text(hub, encoding='utf-8')

    for slug, (label, domain) in TENANTS.items():
        build_tenant(slug, label, domain, main_out)
    for kind, o in OUT.items():
        rewrite_links(o, hosted | set(LOCAL_SITES))
        write_common(o, kind)

    ok = True
    for kind, o in OUT.items():
        size, count = measure(o)
        lim_size, lim_count = LIMITS[kind]
        flag = 'OK' if size <= lim_size and count <= lim_count else 'OVER LIMIT'
        ok = ok and flag == 'OK'
        print(f'{kind}: {size / 1024 / 1024:.1f} MB, {count} files [{flag}]')
    print(f"sites packaged: {len([k for k in report['sites'] if not k.startswith('tenants/')])} | tenant pages: {[k for k in report['sites'] if k.startswith('tenants/')]}")
    for k, v in report['sites'].items():
        if k.startswith('tenants/'):
            print(f'  {k}: {v}')
    print(f"github.io links rewritten: {report['rewrites']}")
    print(f"links to unpublished repos left as-is: {sorted(report['unresolved_links']) or 'none'}")
    print(f"Office files still containing github.io links: {len(report['office_files_with_github_links'])}")
    for f in report['office_files_with_github_links'][:10]:
        print('  ', f)
    for repo, ch in report['overlays'].items():
        print(f'overlay {repo}: {len(ch)} file(s) from local copy: {ch[:6]}')
    if not ok:
        sys.exit('Size or file-count limit exceeded')


if __name__ == '__main__':
    main()

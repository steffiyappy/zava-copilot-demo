# -*- coding: utf-8 -*-
"""Final build pass: align generated hub content with Microsoft Copilot changes
announced up to September 2026 (checked on Microsoft Learn on 23 Sep 2026).

- Copilot Cowork is generally available (16 Jun 2026). Only the App skill and
  choosing GPT 5.5 still need the Frontier Program.
  https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
  https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
- Word, Excel and PowerPoint agents need a paid Microsoft 365 Copilot license.
  https://learn.microsoft.com/en-us/microsoft-365/copilot/wordexcelppt-agents
- Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat.
  https://learn.microsoft.com/en-us/copilot/privacy-and-protections

Source files keep their original labels; only the generated data is rewritten,
so every earlier build step can keep matching the labels it expects.
"""
import json
import re
from collections import Counter

from util import ANY_ACCT, ANY_LIC, FREE_ACCT, FREE_LIC, FRONTIER_LIC, M365_ACCT, M365_LIC

LABELS = {
    '🤝 Cowork (Frontier)': '🤝 Copilot Cowork',
    '📓 Copilot Notebook': '📓 Copilot Notebooks',
    '🏗 Agent Builder (Microsoft 365 Copilot Chat)': '🏗 Agent Builder (Microsoft Copilot Chat)',
    '🆓 Agent Builder (Free Copilot Chat \u2014 public URL knowledge)': '🆓 Agent Builder (Free Copilot Chat: web and OneNote knowledge)',
}
LABEL_KEYS = ('tool', 'toolId', 'label')

_AGENT_TOOL = re.compile(r'(Word|PowerPoint|Excel) Agent')
_COWORK_STILL_FRONTIER = re.compile(r'App skill|build (?:a|an) (?:full-stack )?app|GPT[- ]?5\.5', re.I)
_BM_ID_HINT = re.compile(r'\b(Buka|Tempel|Tampal|dan|pada|untuk|atau)\b')

# Applied to every string, in order. Longer phrases come first so that the
# shorter "Cowork (Frontier)" rule never produces "Copilot Copilot Cowork".
_TEXT_RULES = [
    ('rename_chat', re.compile(r'(?<!name for )(?<!baharu bagi )(?<!baru untuk )Microsoft 365 Copilot Chat'), 'Microsoft Copilot Chat'),
    ('cowork_label', re.compile(re.escape('Open Microsoft 365 Copilot \u2192 left nav \u2192 Agents \u2192 Cowork (Frontier Program required)')),
     'Open Microsoft Copilot \u2192 select Cowork in the toggle next to Chat'),
    ('cowork_label', re.compile(re.escape('Open Microsoft 365 Copilot Cowork (Frontier required)')), 'Open Copilot Cowork'),
    ('cowork_label', re.compile(r'Copilot in Coworker \(Frontier\) mode'), 'Copilot Cowork'),
    ('cowork_label', re.compile(r'(?:Microsoft 365 )?Copilot Cowork(?:er)? \(Frontier\)'), 'Copilot Cowork'),
    ('cowork_label', re.compile(r'Cowork \((?:Frontier Program required|Frontier required|memerlukan Frontier Program)\)'), 'Cowork'),
    ('cowork_label', re.compile(r'Frontier Cowork|Cowork Frontier|Cowork \(Frontier\)'), 'Copilot Cowork'),
    ('cowork_label', re.compile(r'Frontier scheduled tasks'), 'Cowork scheduled tasks'),
    ('cowork_label', re.compile(r'Copilot dalam mode Coworker \(Frontier\)'), 'Copilot Cowork'),
    ('cowork_label', re.compile(r'Cowork \(Frontier(?: program)?, Claude\)'), 'Cowork (Claude model)'),
    ('cowork_label', re.compile(r' \(Frontier program \u2014 Claude\)'), ' (choose a Claude model)'),
    ('cowork_label', re.compile(r'Use Frontier Claude model\.'), 'Use a Claude model.'),
    ('agent_licence', re.compile(r'Works \*\*with or without\*\* a Microsoft 365 Copilot license[^.]*\.'), 'Needs a **Microsoft 365 Copilot** license.'),
    ('agent_licence', re.compile(r'Works with the free Copilot Chat account or an? Microsoft 365 Copilot license\.'), 'Needs a Microsoft 365 Copilot license.'),
    ('agent_licence', re.compile(r'Berfungsi \*\*dengan maupun tanpa\*\* lisensi Microsoft 365 Copilot[^.]*\.'), 'Membutuhkan lisensi **Microsoft 365 Copilot**.'),
    ('agent_licence', re.compile(r'Berfungsi \*\*dengan maupun tanpa\*\* lesen Microsoft 365 Copilot[^.]*\.'), 'Memerlukan lesen **Microsoft 365 Copilot**.'),
    ('agent_licence', re.compile(r'Berfungsi dengan akun Copilot Chat gratis maupun lisensi Microsoft 365 Copilot\.'), 'Membutuhkan lisensi Microsoft 365 Copilot.'),
    ('agent_licence', re.compile(r'Berfungsi dengan akaun Copilot Chat percuma (?:atau|maupun) lesen Microsoft 365 Copilot\.'), 'Memerlukan lesen Microsoft 365 Copilot.'),
]
_COWORK_PATHS_EN = re.compile(r'`m365\.cloud\.microsoft`\s*(?:[>→]\s*)?(?:left[- ](?:nav|rail)\s*[>→]\s*)?\*{0,2}Agents\*{0,2}\s*[>→]\s*\*{0,2}Cowork\*{0,2}')
_COWORK_PATHS_BM_ID = re.compile(r'`m365\.cloud\.microsoft`\s*(?:[>→]\s*)?(?:(?:nav kiri|navigasi kiri|rail kiri)\s*[>→]\s*)?\*{0,2}Agents\*{0,2}\s*[>→]\s*\*{0,2}Cowork\*{0,2}')
_FRONTIER_SENTENCE = re.compile(r'\s*(?:\((?:Frontier Program required|Memerlukan Frontier Program|Membutuhkan Frontier Program)\.?\)'
                                r'|Frontier (?:required|diperlukan)\.|Frontier [Pp]rogram required\.|(?:Membutuhkan|Memerlukan) program Frontier\.)')


def _fix_text(s, stats):
    out = s
    for name, pat, repl in _TEXT_RULES:
        out, n = pat.subn(repl, out)
        if n:
            stats[name] += n
    if 'Cowork' in out:
        if _BM_ID_HINT.search(out):
            out, n = _COWORK_PATHS_BM_ID.subn('`m365.cloud.microsoft` dan pilih **Cowork** pada toggle di sebelah Chat', out)
        else:
            out, n = _COWORK_PATHS_EN.subn('`m365.cloud.microsoft` and select **Cowork** in the toggle next to Chat', out)
        if n:
            stats['cowork_path'] += n
        out, n = _FRONTIER_SENTENCE.subn('', out)
        if n:
            stats['cowork_frontier_sentence'] += n
    out = out.replace('Copilot Copilot Cowork', 'Copilot Cowork')
    return out


def _fix_block(o, stats):
    tool = o.get('tool')
    if not isinstance(tool, str):
        return
    if 'Cowork' in tool and o.get('license') == FRONTIER_LIC:
        prompt_text = json.dumps([o.get(k) for k in ('prompts', 'promptsID', 'promptsBM')], ensure_ascii=False)
        if not _COWORK_STILL_FRONTIER.search(prompt_text):
            o['license'] = M365_LIC
            stats['cowork_licence_to_m365'] += 1
    if _AGENT_TOOL.search(tool):
        if o.get('license') in (ANY_LIC, FREE_LIC):
            o['license'] = M365_LIC
            stats['agent_licence_to_m365'] += 1
        if o.get('account') in (ANY_ACCT, FREE_ACCT):
            o['account'] = M365_ACCT
        for key in ('persona', 'personaID', 'personaBM'):
            if isinstance(o.get(key), list):
                o[key] = ['Mod Admin' if p == 'Sasha Ouellet' else p for p in o[key]]


def _walk(o, stats):
    if isinstance(o, dict):
        _fix_block(o, stats)
        for k, v in list(o.items()):
            if isinstance(v, str):
                if k in LABEL_KEYS and v in LABELS:
                    o[k] = LABELS[v]
                    stats['label'] += 1
                    continue
                nv = _fix_text(v, stats)
                if nv != v:
                    o[k] = nv
            else:
                _walk(v, stats)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, str):
                nv = _fix_text(v, stats)
                if nv != v:
                    o[i] = nv
            else:
                _walk(v, stats)


def refresh_entry(entry, stats=None):
    """Rewrite one generated industry or department entry in place."""
    stats = stats if stats is not None else Counter()
    _walk(entry, stats)
    return stats

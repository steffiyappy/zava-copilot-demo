"""Sweep every tool(T_BUILDER, ...) block to the IHH-style 3-agent shape via tool_builder().

For each entry (ind(...) or dept(...) call), we:
1. Extract its id, name, and files list from the surrounding call.
2. Find its T_BUILDER block via paren-balanced matching.
3. Replace with a tool_builder(...) call carrying 3 contextual agents:
     A) <Name> War Room Agent           — executive/board briefing
     B) <Name> Operational Decision Agent — front-line operational decisions
     C) <Name> Stakeholder Communications Agent — IR / external holding lines

Each agent is fully spec'd: icon, label, name, desc, multi-paragraph
instructions, 3-6 knowledge files (drawn from the entry's `files` list),
knowledgeNote, and 3 realistic test queries.

The General entry is SKIPPED — it already has hand-authored agents.
"""
import re, os, glob, ast

ROOT = r'C:\Users\peiyiyap\zava-copilot-demo'

# ── Helpers ────────────────────────────────────────────────────────────────
def py_repr(s):
    """Repr that always uses the safe Python repr (escapes newlines, quotes, non-ASCII safely)."""
    return repr(s)

def find_balanced(src, open_re, kind='()'):
    """Find all (start, end) of calls beginning where open_re matches and
    ending at the matching close paren.  open_re must include the opening '('."""
    out = []
    for m in open_re.finditer(src):
        # m.end()-1 is at '('
        j = m.end()
        depth = 1
        in_str = None
        while j < len(src) and depth > 0:
            c = src[j]
            if in_str:
                if c == '\\' and j + 1 < len(src):
                    j += 2; continue
                if in_str in ("'",'"') and c == in_str:
                    in_str = None
                elif in_str.startswith('"""') and src[j:j+3] == '"""':
                    in_str = None; j += 3; continue
                elif in_str.startswith("'''") and src[j:j+3] == "'''":
                    in_str = None; j += 3; continue
                j += 1; continue
            if src[j:j+3] in ('"""',"'''"):
                in_str = src[j:j+3]; j += 3; continue
            if c in ("'",'"'):
                in_str = c; j += 1; continue
            if c == '#':
                eol = src.find('\n', j); j = eol + 1 if eol != -1 else len(src); continue
            if c == '(': depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    out.append((m.start(), j + 1)); break
            j += 1
    return out

def get_indent(src, pos):
    line_start = src.rfind('\n', 0, pos) + 1
    line = src[line_start:pos]
    return re.match(r'\s*', line).group(0)

def split_top_args(inner):
    """Split top-level comma-separated args in a Python call body."""
    parts, buf = [], ''
    dp = db = dc = 0
    in_str = None
    i = 0
    while i < len(inner):
        c = inner[i]
        if in_str:
            buf += c
            if c == '\\' and i + 1 < len(inner): buf += inner[i+1]; i += 2; continue
            if (in_str in ("'",'"')) and c == in_str: in_str = None
            elif in_str.startswith('"""') and inner[i:i+3] == '"""':
                in_str = None; buf += inner[i+1:i+3]; i += 3; continue
            elif in_str.startswith("'''") and inner[i:i+3] == "'''":
                in_str = None; buf += inner[i+1:i+3]; i += 3; continue
            i += 1; continue
        if inner[i:i+3] in ('"""',"'''"):
            in_str = inner[i:i+3]; buf += inner[i:i+3]; i += 3; continue
        if c in ("'",'"'):
            in_str = c; buf += c; i += 1; continue
        if c == '#':
            eol = inner.find('\n', i)
            if eol == -1: buf += inner[i:]; break
            buf += inner[i:eol]; i = eol; continue
        if c == '(': dp += 1
        elif c == ')': dp -= 1
        elif c == '[': db += 1
        elif c == ']': db -= 1
        elif c == '{': dc += 1
        elif c == '}': dc -= 1
        if c == ',' and dp == db == dc == 0:
            parts.append(buf.strip()); buf = ''; i += 1; continue
        buf += c; i += 1
    if buf.strip():
        parts.append(buf.strip())
    return parts

def safe_eval_literal(text):
    """Try to ast.literal_eval; return None on failure."""
    try:
        return ast.literal_eval(text)
    except Exception:
        return None

# ── Entry discovery ────────────────────────────────────────────────────────
RE_IND  = re.compile(r"\bind\s*\(", re.M)
RE_DEPT = re.compile(r"\bdept\s*\(", re.M)
RE_BUILDER_CALL = re.compile(r"tool\s*\(\s*T_BUILDER\s*,")
RE_TOOL_BUILDER = re.compile(r"tool_builder\s*\(")

def parse_entry(call_src):
    """Given the full ind(...) or dept(...) source, extract id, name, files.

    Supports BOTH positional-style and keyword-style entry calls.
    """
    open_ = call_src.index('(')
    close_ = call_src.rfind(')')
    inner = call_src[open_ + 1:close_]
    parts = split_top_args(inner)
    pos, kw = [], {}
    seen_kw = False
    for p in parts:
        m_kw = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=', p)
        if m_kw:
            seen_kw = True
            kw[m_kw.group(1)] = p[m_kw.end():].lstrip()
        elif not seen_kw:
            pos.append(p)
    # Try keyword-style first
    eid   = safe_eval_literal(kw.get('id', '')) if 'id' in kw else None
    name  = safe_eval_literal(kw.get('name', '')) if 'name' in kw else None
    files = safe_eval_literal(kw.get('files', '')) if 'files' in kw else None
    # Fall back to positional (ind signature: id,sector,name,icon,c1,c2,company,tagline,scenario,files)
    if eid is None and len(pos) >= 1: eid = safe_eval_literal(pos[0])
    if name is None and len(pos) >= 3: name = safe_eval_literal(pos[2])
    if files is None and len(pos) >= 10: files = safe_eval_literal(pos[9])
    if not isinstance(eid, str) or not isinstance(name, str):
        return None
    if not isinstance(files, list):
        files = []
    return {'id': eid, 'name': name, 'files': files}

# ── Agent template generator ───────────────────────────────────────────────
ICONS = ['🏛️', '⚙️', '📣']

def strip_emoji_prefix(name):
    # Drop a leading emoji + space (e.g., "⚖️ Legal" → "Legal")
    return re.sub(r'^[^\w\(\[]+\s*', '', name).strip() or name

def make_agents(entry, lang='EN'):
    name = strip_emoji_prefix(entry['name'])
    files = entry['files'] or []
    # Pick up to 6 files for War Room, 4 for Ops, 4 for Comms
    f_war = files[:6] if files else []
    f_ops = files[:4] if files else []
    f_com = files[:4] if files else []

    if lang == 'EN':
        return [
            {
                'icon': ICONS[0],
                'label': f'{name} War Room Agent',
                'name':  f'Zava {name} War Room Agent',
                'desc':  f'You are an executive briefing agent for the {name} leadership team — board, CEO, CFO and Chief of Staff — during the live scenario for this entry.',
                'instructions': (
                    f"You are the Zava {name} War Room agent. You support the {name} leadership — board, CEO, CFO and Chief of Staff — through the live scenario described on this page.\n\n"
                    "When answering questions:\n"
                    "• Ground every quantitative claim in the spreadsheets attached to this scenario and ALWAYS cite the file name and tab/section.\n"
                    "• Ground every governance, policy or strategy claim in the docx files attached and cite the section number.\n"
                    "• Classify each recommendation as Red (act in 24 hours), Amber (act this week) or Green (monitor) by board materiality.\n"
                    "• Tone is precise, board-ready, never speculative.  Use short sentences.  Use markdown tables when comparing options or scenarios.\n\n"
                    "When drafting holding lines (lender, regulator, investor):\n"
                    "• Use defensible facts only.  Flag any number the source files cannot substantiate.\n"
                    "• Always include a one-line escalation path (\"If pressed further, refer to <named owner>\").\n\n"
                    "If the user asks a question outside your knowledge base, refuse politely and say: \"I don't have that in my current knowledge base; please contact the relevant team.\""
                ),
                'knowledge': [{'file': f, 'note': 'Reference file for this scenario — primary source for any cited number or policy clause.'} for f in f_war],
                'knowledgeNote': f"After uploading, ask the agent: \"Which file would you cite for the headline figure in the {name} scenario?\" — confirm it names the right reference file and tab.",
                'queries': [
                    f"Summarise the headline issue facing {name} in 60 seconds for the Board — name the top 3 risks, the largest variance driver, and the single Red action the Board must approve in this meeting. Cite source files for every number.",
                    f"Draft a 4-line holding line for the lead relationship banks (CIMB, Maybank, Mandiri, BCA) on the current {name} position. Use only the figures in the attached files and flag any facility within 10% of breach. Tone: conservative, lender-facing.",
                    f"What governance obligations apply to the current {name} situation? Quote the exact policy clause and tell me which director-level approvals are required before any external disclosure.",
                ],
            },
            {
                'icon': ICONS[1],
                'label': f'{name} Operational Decision Agent',
                'name':  f'Zava {name} Operational Decision Agent',
                'desc':  f'You support the front-line {name} operating team with day-to-day decisions, KPI checks, and exception handling, grounded on the operational data attached.',
                'instructions': (
                    f"You are the Zava {name} Operational Decision agent.  You support the front-line operating team for {name} with day-to-day decisions, KPI tracking, and exception handling.\n\n"
                    "When answering questions:\n"
                    "• Ground every metric, threshold or KPI in the attached spreadsheets and cite the file + tab.\n"
                    "• When a value sits outside a tolerance band, classify it as In Tolerance / Watch / Action Required and recommend ONE next step.\n"
                    "• Tone is operational, concise, action-oriented.  Use bulleted action items wherever possible.\n\n"
                    "When asked about exceptions:\n"
                    "• Always reference the relevant policy clause from the attached docx.\n"
                    "• Recommend the named approver (role only — no individual names) per the delegation of authority.\n\n"
                    "If the user asks for board-level disclosure language, regulator-facing statements, or HR matters, refuse politely and refer them to the {name} War Room agent or the Stakeholder Communications agent."
                ),
                'knowledge': [{'file': f, 'note': 'Operational data and policy reference for day-to-day decisions.'} for f in f_ops],
                'knowledgeNote': f"Test query: \"What is the current status of the top operational KPI for {name}?\" — agent should cite the file and tab, give the value vs target, and a one-line corrective action if outside tolerance.",
                'queries': [
                    f"What are the top 5 operational KPIs for {name} this week? Tabulate name, current value, target, variance %, status (In Tolerance / Watch / Action Required), and recommended next step. Cite files.",
                    f"List every exception that has breached its policy threshold this week, with the originating department, the breached clause, and the named approver role required to authorise the exception.",
                    f"Build me the next-day shift handover note for {name} — top 3 in-flight issues, owner, expected resolution time, escalation contact role.",
                ],
            },
            {
                'icon': ICONS[2],
                'label': f'{name} Stakeholder Communications Agent',
                'name':  f'Zava {name} Stakeholder Communications Agent',
                'desc':  f'You draft external responses (analyst, investor, media, regulator) for the {name} Head of Communications and Group Chief of Staff during sensitive periods.',
                'instructions': (
                    f"You are the Zava {name} Stakeholder Communications agent.  You support the Head of Communications and the Group Chief of Staff in drafting external responses during sensitive periods.\n\n"
                    "When drafting any external response:\n"
                    "• Use only language that is already in the approved Q&A or strategy framework attached — never invent a forward-looking statement.\n"
                    "• Quote every figure to the source spreadsheet and tab.\n"
                    "• Filter every draft through the disclosure clauses in the attached policy handbook.\n"
                    "• Tone is factual, conservative, never forward-looking unless the source already disclosed it.  Avoid superlatives.  Short paragraphs.\n\n"
                    "When asked for forward guidance:\n"
                    "• Default response: \"The Group has not yet provided forward guidance on this point.  The next scheduled update is at <next-disclosure-date from policy handbook>.\"\n\n"
                    "If a question requires legal interpretation or a regulator-facing statement, refuse politely and say: \"That requires Legal & Corporate Secretarial review before any external response.  I can draft a holding line in the meantime — would you like one?\""
                ),
                'knowledge': [{'file': f, 'note': 'Pre-approved Q&A, strategy framework, or disclosure policy for external messaging.'} for f in f_com],
                'knowledgeNote': f"Test query: \"Draft a 200-word reply to a sell-side question about {name} forward guidance.\" — the agent should refuse to give a number and offer policy-compliant holding language, citing the disclosure clause.",
                'queries': [
                    f"A sell-side analyst has emailed asking about forward guidance on {name}.  Draft a 200-word policy-compliant reply: refuse to give a number, point to the next scheduled disclosure, and reference the strategy framework's medium-term direction.  Cite the policy clause that governs your response.",
                    f"Build me a 10-question analyst Q&A pack for the next earnings call covering {name} — performance, drivers, capital allocation, ESG, and regulator engagement.  For each, give the suggested 4-line answer and the source-file citation.",
                    f"Draft a 3-line holding line for a journalist asking about the current {name} situation.  Use only language already approved in the attached Q&A document.",
                ],
            },
        ]
    elif lang == 'ID':
        return [
            {
                'icon': ICONS[0],
                'label': f'Agent War Room {name}',
                'name':  f'Zava Agent War Room {name}',
                'desc':  f'Anda adalah agent briefing tingkat eksekutif untuk tim kepemimpinan {name} — Direksi, Direktur Utama, Direktur Keuangan, dan Kepala Staf — selama skenario aktif di halaman ini.',
                'instructions': (
                    f"Anda adalah agent Zava {name} War Room. Anda mendukung kepemimpinan {name} — Direksi, Direktur Utama, Direktur Keuangan, dan Kepala Staf — melalui skenario aktif di halaman ini.\n\n"
                    "Saat menjawab pertanyaan:\n"
                    "• Dasarkan tiap klaim kuantitatif pada spreadsheet yang dilampirkan dan SELALU kutip nama file dan tab/bagian.\n"
                    "• Dasarkan tiap klaim tata kelola, kebijakan atau strategi pada file docx yang dilampirkan dengan nomor bagian.\n"
                    "• Klasifikasikan tiap rekomendasi sebagai Merah (tindak dalam 24 jam), Kuning (tindak minggu ini), atau Hijau (pantau) berdasarkan materialitas Direksi.\n"
                    "• Nada presisi, siap-Direksi, tidak spekulatif. Kalimat pendek. Gunakan tabel markdown saat membandingkan opsi atau skenario.\n\n"
                    "Jika pertanyaan di luar basis pengetahuan Anda, tolak dengan sopan: \"Itu tidak ada di basis pengetahuan saya; silakan hubungi tim terkait.\""
                ),
                'knowledge': [{'file': f, 'note': 'File referensi untuk skenario ini — sumber utama angka atau klausul kebijakan.'} for f in f_war],
                'knowledgeNote': f'Setelah upload, tanya: "File mana yang Anda kutip untuk angka utama dalam skenario {name}?" — pastikan agent menyebut file referensi yang benar dan tab.',
                'queries': [
                    f"Rangkum isu utama yang dihadapi {name} dalam 60 detik untuk Direksi — sebutkan 3 risiko teratas, driver selisih terbesar, dan satu tindakan Merah yang harus disetujui Direksi pada rapat ini. Kutip file sumber untuk tiap angka.",
                    f"Susun holding line 4 baris untuk bank relasi utama (CIMB, Maybank, Mandiri, BCA) terkait posisi {name} saat ini. Hanya gunakan angka di file lampiran dan tandai fasilitas yang berada dalam 10% jarak breach.",
                    f"Kewajiban tata kelola apa yang berlaku pada situasi {name} saat ini? Kutip klausul kebijakan tepat dan beritahu saya persetujuan tingkat direktur mana yang diperlukan sebelum pengungkapan eksternal.",
                ],
            },
            {
                'icon': ICONS[1],
                'label': f'Agent Keputusan Operasional {name}',
                'name':  f'Zava Agent Keputusan Operasional {name}',
                'desc':  f'Anda mendukung tim operasional {name} dengan keputusan harian, pemeriksaan KPI, dan penanganan eksepsi, berdasarkan data operasional yang dilampirkan.',
                'instructions': (
                    f"Anda adalah agent Zava Keputusan Operasional {name}. Anda mendukung tim operasional garis-depan {name} dengan keputusan harian, pelacakan KPI, dan penanganan eksepsi.\n\n"
                    "Saat menjawab:\n"
                    "• Dasarkan tiap metrik, ambang batas, atau KPI pada spreadsheet lampiran dan kutip file + tab.\n"
                    "• Bila nilai keluar dari toleransi, klasifikasikan sebagai In Tolerance / Watch / Action Required dan rekomendasikan SATU langkah berikutnya.\n"
                    "• Nada operasional, ringkas, action-oriented. Gunakan bullet point.\n\n"
                    "Jika diminta bahasa pengungkapan tingkat Direksi, pernyataan untuk regulator, atau urusan SDM, tolak dengan sopan dan rujuk ke agent War Room atau Stakeholder Communications."
                ),
                'knowledge': [{'file': f, 'note': 'Data operasional dan referensi kebijakan untuk keputusan harian.'} for f in f_ops],
                'knowledgeNote': f'Uji query: "Apa status KPI operasional teratas untuk {name} saat ini?" — agent harus mengutip file dan tab, memberi nilai vs target, dan tindakan satu baris bila di luar toleransi.',
                'queries': [
                    f"Apa 5 KPI operasional teratas untuk {name} minggu ini? Tabulasikan nama, nilai saat ini, target, selisih %, status (In Tolerance / Watch / Action Required), dan langkah berikutnya. Kutip file.",
                    f"Daftarkan tiap eksepsi yang melanggar ambang kebijakan minggu ini, dengan departemen asal, klausul yang dilanggar, dan peran approver yang diperlukan untuk mengotorisasi eksepsi.",
                    f"Susun catatan serah-terima shift hari berikutnya untuk {name} — 3 isu in-flight teratas, owner, perkiraan waktu resolusi, kontak eskalasi.",
                ],
            },
            {
                'icon': ICONS[2],
                'label': f'Agent Komunikasi Pemangku Kepentingan {name}',
                'name':  f'Zava Agent Komunikasi Pemangku Kepentingan {name}',
                'desc':  f'Anda menyusun respons eksternal (analis, investor, media, regulator) untuk Kepala Komunikasi {name} dan Kepala Staf Grup selama periode sensitif.',
                'instructions': (
                    f"Anda adalah agent Zava Komunikasi Pemangku Kepentingan {name}. Anda mendukung Kepala Komunikasi dan Kepala Staf Grup dalam menyusun respons eksternal selama periode sensitif.\n\n"
                    "Saat menyusun respons eksternal:\n"
                    "• Hanya gunakan bahasa yang sudah ada di Q&A yang disetujui atau strategy framework yang dilampirkan — tidak pernah membuat pernyataan forward-looking baru.\n"
                    "• Kutip tiap angka ke spreadsheet sumber dan tab.\n"
                    "• Saring tiap draf melalui klausul pengungkapan di policy handbook.\n"
                    "• Nada faktual, konservatif, tidak forward-looking kecuali sumber sudah mengungkapkan.\n\n"
                    "Jika diminta panduan ke depan, default response: \"Grup belum memberikan panduan ke depan untuk hal ini. Update terjadwal berikutnya pada <tanggal-pengungkapan dari policy handbook>.\""
                ),
                'knowledge': [{'file': f, 'note': 'Q&A pra-disetujui, strategy framework, atau kebijakan pengungkapan untuk pesan eksternal.'} for f in f_com],
                'knowledgeNote': f'Uji query: "Susun jawaban 200 kata untuk pertanyaan sell-side mengenai panduan ke depan {name}." — agent harus menolak memberi angka dan menawarkan bahasa holding sesuai kebijakan.',
                'queries': [
                    f"Analis sell-side mengirim email meminta panduan ke depan untuk {name}. Susun jawaban 200 kata yang patuh kebijakan: tolak memberi angka, rujuk pada pengungkapan terjadwal berikutnya, dan referensikan arah jangka menengah strategy framework. Kutip klausul kebijakan.",
                    f"Bangun pack Q&A analis 10 pertanyaan untuk earnings call berikutnya mencakup {name} — kinerja, driver, alokasi modal, ESG, engagement regulator. Untuk masing-masing, beri jawaban 4 baris dan kutipan file sumber.",
                    f"Susun holding line 3 baris untuk wartawan yang bertanya tentang situasi {name} saat ini. Hanya gunakan bahasa yang sudah disetujui di dokumen Q&A lampiran.",
                ],
            },
        ]
    return []

# ── Build the tool_builder() call source ───────────────────────────────────
def fmt_agent(a, indent_str):
    inner = indent_str + '    '
    knowledge_lines = []
    for k in a['knowledge']:
        knowledge_lines.append(
            f"{inner}  {{'file':{py_repr(k['file'])}, 'note':{py_repr(k['note'])}}}"
        )
    knowledge_block = '[\n' + ',\n'.join(knowledge_lines) + f'\n{inner}]' if knowledge_lines else '[]'
    queries_lines = [f"{inner}  {py_repr(q)}" for q in a['queries']]
    queries_block = '[\n' + ',\n'.join(queries_lines) + f'\n{inner}]' if queries_lines else '[]'

    return (
        f"{indent_str}  {{\n"
        f"{inner}'icon': {py_repr(a['icon'])},\n"
        f"{inner}'label': {py_repr(a['label'])},\n"
        f"{inner}'name': {py_repr(a['name'])},\n"
        f"{inner}'desc': {py_repr(a['desc'])},\n"
        f"{inner}'instructions': {py_repr(a['instructions'])},\n"
        f"{inner}'knowledge': {knowledge_block},\n"
        f"{inner}'knowledgeNote': {py_repr(a['knowledgeNote'])},\n"
        f"{inner}'queries': {queries_block},\n"
        f"{indent_str}  }}"
    )

def build_tool_builder_call(entry, lic_arg, acct_arg, persona, personaID, indent):
    agents_en = make_agents(entry, 'EN')
    agents_id = make_agents(entry, 'ID')
    en_block = '[\n' + ',\n'.join(fmt_agent(a, indent) for a in agents_en) + f'\n{indent}]'
    id_block = '[\n' + ',\n'.join(fmt_agent(a, indent) for a in agents_id) + f'\n{indent}]'
    out = ['tool_builder(' + lic_arg + ', ' + acct_arg + ',',
           indent + '  agents=' + en_block + ',',
           indent + '  agentsID=' + id_block + ',']
    if persona:
        out.append(indent + '  persona=' + repr(persona) + ',')
    if personaID:
        out.append(indent + '  personaID=' + repr(personaID) + ',')
    out[-1] = out[-1].rstrip(',')
    out.append(indent + ')')
    return '\n'.join(out)

# ── Main sweep ─────────────────────────────────────────────────────────────
files = sorted(glob.glob(os.path.join(ROOT, 'ind_batch*.py')) +
               glob.glob(os.path.join(ROOT, 'dept_data*.py')))

ENTRY_OPENERS = re.compile(r"\b(?:ind|dept)\s*\(", re.M)
total = 0

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    # Find all entry calls (ind/dept)
    entry_blocks = find_balanced(src, ENTRY_OPENERS)
    if not entry_blocks:
        continue
    # Walk RIGHT-TO-LEFT so offsets remain valid
    new_src = src
    rewrote = 0
    for e_start, e_end in reversed(entry_blocks):
        entry_src = new_src[e_start:e_end]
        meta = parse_entry(entry_src)
        if not meta:
            continue
        # Skip the General entry — already done by hand
        if meta['id'] == 'general':
            continue
        # Find T_BUILDER block(s) within this entry
        sub_offset = e_start
        # Search for builder blocks within entry_src
        builder_blocks = []
        for m in RE_BUILDER_CALL.finditer(entry_src):
            j = m.end() - 1   # at '('
            # Walk to balanced close, accounting for strings
            depth = 1; jj = j + 1; in_str = None
            while jj < len(entry_src) and depth > 0:
                c = entry_src[jj]
                if in_str:
                    if c == '\\' and jj + 1 < len(entry_src): jj += 2; continue
                    if in_str in ("'",'"') and c == in_str: in_str = None
                    elif in_str.startswith('"""') and entry_src[jj:jj+3] == '"""': in_str = None; jj += 3; continue
                    elif in_str.startswith("'''") and entry_src[jj:jj+3] == "'''": in_str = None; jj += 3; continue
                    jj += 1; continue
                if entry_src[jj:jj+3] in ('"""',"'''"): in_str = entry_src[jj:jj+3]; jj += 3; continue
                if c in ("'",'"'): in_str = c; jj += 1; continue
                if c == '#':
                    eol = entry_src.find('\n', jj); jj = eol + 1 if eol != -1 else len(entry_src); continue
                if c == '(': depth += 1
                elif c == ')':
                    depth -= 1
                    if depth == 0: builder_blocks.append((m.start(), jj + 1)); break
                jj += 1
        if not builder_blocks:
            continue
        # Replace each builder block from right-to-left
        for b_start_rel, b_end_rel in reversed(builder_blocks):
            b_start = sub_offset + b_start_rel
            b_end = sub_offset + b_end_rel
            block_src = new_src[b_start:b_end]
            # Extract lic + acct + persona/personaID
            open_ = block_src.index('(')
            close_ = block_src.rfind(')')
            inner = block_src[open_ + 1:close_]
            parts = split_top_args(inner)
            pos = []; kw = {}
            for p in parts:
                m_kw = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=', p)
                if m_kw:
                    kw[m_kw.group(1)] = p[m_kw.end():].lstrip()
                else:
                    pos.append(p)
            if len(pos) < 3:
                continue
            lic_arg = pos[1].strip()
            acct_arg = pos[2].strip()
            # Cap personas to 3
            def cap(rkw, default='Mod Admin'):
                if not rkw: return None
                arr = safe_eval_literal(rkw)
                if isinstance(arr, list):
                    arr = (arr + [default]*3)[:3]
                    return arr
                return None
            persona   = cap(kw.get('persona'))
            personaID = cap(kw.get('personaID'))
            indent = get_indent(new_src, b_start)
            new_call = build_tool_builder_call(meta, lic_arg, acct_arg, persona, personaID, indent)
            new_src = new_src[:b_start] + new_call + new_src[b_end:]
            rewrote += 1
    if rewrote and new_src != src:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_src)
        print(f'  rewrote {rewrote:>2} block(s) in {os.path.basename(path)}')
    total += rewrote

print(f'\nTotal builder blocks rewritten: {total}')

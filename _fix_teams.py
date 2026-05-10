"""Sweep every tool(T_TEAMS, ...) block to the canonical IHH-style 3-meeting structure.

Pattern per prompt (3 prompts per block — one per meeting):
  INSTR: (1) Open Teams Calendar → meeting → walk through AI Notes / Custom summary / Audio recap.
         (2) Open Word for the Web → new doc → type minutes template skeleton.
         (3) Open Copilot pane in Word → paste PROMPT.
  PROMPT: "Create meeting minutes for the Teams meeting /<name>. Use the empty template ... Save as Minutes_<safe>.docx."

3 canonical meetings, in order:
  M1: New Software Implementation
  M2: Marketing Campaign Performance Review
  M3: Negotiating Marketing Contract
"""
import re, os, glob

ROOT = r'C:\Users\peiyiyap\zava-copilot-demo'

# ── Canonical 3-meeting blocks ─────────────────────────────────────────────
EN = [
    {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"New Software Implementation"**. On the Recap page, walk the audience through the **AI Notes** (auto-summary), the **Custom summary** (Copilot\'s per-attendee view), and the **Audio recap** (chapter markers with speaker timings). **(2) In Word for the Web**, open a **new blank document**. Type a minutes template at the top — five empty headings: Date and Attendees · Agenda Items · Decisions Taken · Action Items · Risks and Open Questions. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — Copilot in Word will reference the meeting recap by name with `/` and fill the template.',
     'prompt':'Create meeting minutes for the Teams meeting /New Software Implementation. Use the empty template already on this page and fill each heading from the meeting recap. Sections: (1) Date and Attendees; (2) Agenda Items; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Risks and Open Questions. Quote attendee statements verbatim where the wording matters. Tag any decision that is on the critical path as Critical Path. Save the file as Minutes_New_Software_Implementation.docx in OneDrive.'},
    {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Marketing Campaign Performance Review"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap** chapters. **(2) In Word for the Web**, open a **new blank document**. Type a campaign-review minutes template at the top — six empty headings: Date and Attendees · Campaign KPIs Reviewed · Decisions Taken · Action Items · Budget Reallocations · Next Review Date. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below.',
     'prompt':'Create meeting minutes for the Teams meeting /Marketing Campaign Performance Review. Use the empty campaign-review template already on this page. Sections: (1) Date and Attendees; (2) Campaign KPIs Reviewed; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Budget Reallocations Approved; (6) Next Review Date. Quote attendee statements verbatim where the wording matters. Highlight any KPI that missed target by more than 10% in amber. Save the file as Minutes_Marketing_Campaign_Review.docx in OneDrive.'},
    {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Negotiating Marketing Contract"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap**. **(2) In Word for the Web**, open a **new blank document**. Type a vendor-negotiation minutes template at the top — seven empty headings: Vendor and Owner · Commercial Terms Discussed · Concessions Offered · Concessions Accepted · Open Items · Approval Thresholds · Next Steps. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — then forward the result to Procurement, Legal, and the Group CFO.',
     'prompt':'Create meeting minutes for the Teams meeting /Negotiating Marketing Contract. Use the empty vendor-negotiation template already on this page. Sections: (1) Vendor and Owner; (2) Commercial Terms Discussed; (3) Concessions Offered; (4) Concessions Accepted; (5) Open Items; (6) Approval Thresholds (CFO / Board); (7) Next Steps with Owner and Due Date. Highlight any term requiring CFO sign-off in amber and any term requiring Board sign-off in red. Save the file as Minutes_Marketing_Contract_Negotiation.docx in OneDrive and email the link to Procurement, Legal, and the Group CFO.'},
]

ID = [
    {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"New Software Implementation"**. Di halaman Recap, jelaskan ke peserta tentang **AI Notes** (ringkasan otomatis), **Custom summary** (tampilan per-peserta dari Copilot), dan **Audio recap** (penanda bab dengan timing pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baru**. Ketik kerangka notulen di bagian atas — lima heading kosong: Tanggal dan Peserta · Agenda · Keputusan · Action Items · Risiko dan Pertanyaan Terbuka. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — Copilot in Word akan merujuk recap rapat dengan `/` dan mengisi template.',
     'prompt':'Susun notulen rapat untuk rapat Teams /New Software Implementation. Gunakan template kosong yang sudah ada di halaman ini dan isi tiap heading dari recap rapat. Bagian: (1) Tanggal dan Peserta; (2) Agenda; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Risiko dan Pertanyaan Terbuka. Kutip pernyataan peserta apa adanya bila kata-katanya penting. Tandai keputusan di jalur kritis sebagai Critical Path. Simpan file sebagai Minutes_New_Software_Implementation.docx di OneDrive.'},
    {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Marketing Campaign Performance Review"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen tinjauan kampanye — enam heading kosong: Tanggal dan Peserta · KPI Kampanye yang Dikaji · Keputusan · Action Items · Realokasi Anggaran · Jadwal Tinjauan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah.',
     'prompt':'Susun notulen rapat untuk rapat Teams /Marketing Campaign Performance Review. Gunakan template kosong tinjauan kampanye yang sudah ada. Bagian: (1) Tanggal dan Peserta; (2) KPI Kampanye yang Dikaji; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Realokasi Anggaran yang Disetujui; (6) Jadwal Tinjauan Berikutnya. Kutip pernyataan peserta apa adanya. Tandai KPI yang meleset >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive.'},
    {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Negotiating Marketing Contract"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen negosiasi vendor — tujuh heading kosong: Vendor dan Owner · Term Komersial · Konsesi yang Ditawarkan · Konsesi yang Diterima · Item Terbuka · Threshold Persetujuan · Langkah Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — kemudian teruskan hasilnya ke Procurement, Legal, dan Direktur Keuangan Grup.',
     'prompt':'Susun notulen rapat untuk rapat Teams /Negotiating Marketing Contract. Gunakan template kosong negosiasi vendor yang sudah ada. Bagian: (1) Vendor dan Owner; (2) Term Komersial; (3) Konsesi yang Ditawarkan; (4) Konsesi yang Diterima; (5) Item Terbuka; (6) Threshold Persetujuan (CFO / Direksi); (7) Langkah Berikutnya dengan Owner dan Due Date. Tandai term yang memerlukan persetujuan CFO dengan amber dan persetujuan Direksi dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive lalu email link-nya ke Procurement, Legal, dan Direktur Keuangan Grup.'},
]

BM = [
    {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"New Software Implementation"**. Pada halaman Recap, terangkan kepada hadirin tentang **AI Notes** (ringkasan automatik), **Custom summary** (paparan per-hadirin dari Copilot), dan **Audio recap** (penanda bab dengan masa pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baharu**. Taip rangka minit di bahagian atas — lima tajuk kosong: Tarikh dan Hadirin · Agenda · Keputusan · Tindakan · Risiko dan Soalan Terbuka. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — Copilot in Word akan merujuk recap mesyuarat dengan `/` dan mengisi templat.',
     'prompt':'Hasilkan minit mesyuarat untuk mesyuarat Teams /New Software Implementation. Gunakan templat kosong yang sudah ada di halaman ini dan isi setiap tajuk daripada recap mesyuarat. Bahagian: (1) Tarikh dan Hadirin; (2) Agenda; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Risiko dan Soalan Terbuka. Petik kenyataan hadirin sebagaimana asal di mana perkataannya penting. Tandakan sebarang keputusan di laluan kritikal sebagai Critical Path. Simpan fail sebagai Minutes_New_Software_Implementation.docx di OneDrive.'},
    {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Marketing Campaign Performance Review"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit ulasan kempen — enam tajuk kosong: Tarikh dan Hadirin · KPI Kempen yang Diulas · Keputusan · Tindakan · Pelarasan Bajet · Tarikh Ulasan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah.',
     'prompt':'Hasilkan minit mesyuarat untuk mesyuarat Teams /Marketing Campaign Performance Review. Gunakan templat kosong ulasan kempen yang sudah ada. Bahagian: (1) Tarikh dan Hadirin; (2) KPI Kempen yang Diulas; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Pelarasan Bajet yang Diluluskan; (6) Tarikh Ulasan Berikutnya. Petik kenyataan hadirin sebagaimana asal. Tandakan KPI yang tersasar >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive.'},
    {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Negotiating Marketing Contract"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit perundingan vendor — tujuh tajuk kosong: Vendor dan Pemilik · Terma Komersial · Konsesi Ditawarkan · Konsesi Diterima · Item Terbuka · Ambang Kelulusan · Langkah Seterusnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — kemudian majukan hasilnya kepada Procurement, Legal dan Pengarah Kewangan Kumpulan.',
     'prompt':'Hasilkan minit mesyuarat untuk mesyuarat Teams /Negotiating Marketing Contract. Gunakan templat kosong perundingan vendor yang sudah ada. Bahagian: (1) Vendor dan Pemilik; (2) Terma Komersial; (3) Konsesi Ditawarkan; (4) Konsesi Diterima; (5) Item Terbuka; (6) Ambang Kelulusan (CFO / Lembaga); (7) Langkah Seterusnya dengan Pemilik dan Tarikh. Tandakan terma yang memerlukan kelulusan CFO dengan amber dan Lembaga dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive dan e-mel pautan kepada Procurement, Legal dan Pengarah Kewangan Kumpulan.'},
]

# ── Helpers ────────────────────────────────────────────────────────────────
def py_repr(s):
    """Render a string in Python source: prefer double-quoted unless string has unescaped double quotes."""
    # Use single-quote with escapes when the string contains double quotes
    if '"' in s and "'" not in s:
        return "'" + s.replace("\\","\\\\").replace("'","\\'") + "'"
    if '"' in s:
        # mix — escape everything in double-quoted string
        return '"' + s.replace("\\","\\\\").replace('"','\\"') + '"'
    return '"' + s.replace("\\","\\\\").replace('"','\\"') + '"'

def fmt_prompt_dicts(arr, indent_str):
    inner_indent = indent_str + '  '
    item_lines = []
    for d in arr:
        item_lines.append(
            f"{inner_indent}{{'instr':{py_repr(d['instr'])}, 'prompt':{py_repr(d['prompt'])}}}"
        )
    return '[\n' + ',\n'.join(item_lines) + f'\n{indent_str}]'

# Find all `tool(T_TEAMS, <args>)` calls — paren-balanced
def find_team_blocks(src):
    blocks = []
    pat = re.compile(r'tool\(\s*T_TEAMS\s*,')
    for m in pat.finditer(src):
        start = m.start()
        i = m.end() - 1   # at the comma
        # scan forward, count parens, respecting strings/comments lightly
        depth = 1
        j = i + 1
        in_str = None    # None, "'", '"', or triple variants
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
            # not in string
            if src[j:j+3] in ('"""',"'''"):
                in_str = src[j:j+3]
                j += 3; continue
            if c in ("'",'"'):
                in_str = c; j += 1; continue
            if c == '#':
                # to end of line
                eol = src.find('\n', j)
                j = eol + 1 if eol != -1 else len(src)
                continue
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    blocks.append((start, j + 1))
                    break
            j += 1
    return blocks

def get_indent(src, pos):
    # Indent = leading whitespace of the line containing pos
    line_start = src.rfind('\n', 0, pos) + 1
    line = src[line_start:pos]
    return re.match(r'\s*', line).group(0)

def split_tool_args(call_src):
    """Given source like `tool(T_TEAMS, ARG1, ARG2, [...prompts...], desc, promptsID=[...], ...)`
    return (positional_args_text, kwargs_dict_keeping_source_text).
    We do this by walking tokens at depth=1 inside the outer parens, splitting on commas.
    """
    # Slice to interior between outermost parens
    open_ = call_src.index('(')
    close_ = call_src.rfind(')')
    inner = call_src[open_ + 1:close_]
    # Walk and split top-level commas
    parts, buf = [], ''
    depth_p = depth_b = depth_c = 0
    in_str = None
    i = 0
    while i < len(inner):
        c = inner[i]
        if in_str:
            buf += c
            if c == '\\' and i + 1 < len(inner):
                buf += inner[i + 1]; i += 2; continue
            if (in_str in ("'", '"')) and c == in_str:
                in_str = None
            elif in_str.startswith('"""') and inner[i:i+3] == '"""':
                in_str = None; buf += inner[i+1:i+3]; i += 3; continue
            elif in_str.startswith("'''") and inner[i:i+3] == "'''":
                in_str = None; buf += inner[i+1:i+3]; i += 3; continue
            i += 1; continue
        if inner[i:i+3] in ('"""',"'''"):
            in_str = inner[i:i+3]; buf += inner[i:i+3]; i += 3; continue
        if c in ("'", '"'):
            in_str = c; buf += c; i += 1; continue
        if c == '#':
            # consume to end of line
            eol = inner.find('\n', i)
            if eol == -1:
                buf += inner[i:]; break
            buf += inner[i:eol]; i = eol; continue
        if c == '(': depth_p += 1
        elif c == ')': depth_p -= 1
        elif c == '[': depth_b += 1
        elif c == ']': depth_b -= 1
        elif c == '{': depth_c += 1
        elif c == '}': depth_c -= 1
        if c == ',' and depth_p == 0 and depth_b == 0 and depth_c == 0:
            parts.append(buf.strip())
            buf = ''
            i += 1; continue
        buf += c
        i += 1
    if buf.strip():
        parts.append(buf.strip())
    # Categorise positional vs keyword
    pos = []
    kw = {}
    for p in parts:
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=', p)
        if m:
            key = m.group(1)
            val = p[m.end():].lstrip()
            kw[key] = val
        else:
            pos.append(p)
    return pos, kw

def replace_block(src, start, end, new_call):
    return src[:start] + new_call + src[end:]

def build_new_call(orig, indent):
    """Given the original tool(T_TEAMS, ...) source, build the canonical replacement."""
    pos, kw = split_tool_args(orig)
    # pos: [T_TEAMS, lic, acct, prompts_list, optional_desc]
    # We keep T_TEAMS, lic, acct.  Replace prompts.
    if len(pos) < 3:
        return orig
    lic_arg = pos[1].strip()
    acct_arg = pos[2].strip()
    # desc — keep if user supplied (4th positional or 'desc=')
    desc_arg = ''
    if len(pos) >= 5:
        desc_arg = pos[4].strip()
    if 'desc' in kw:
        desc_arg = kw['desc'].strip()
    if not desc_arg or desc_arg in ("''", '""', "''", '"DESC_TEAMS"', "'DESC_TEAMS'"):
        # Default keeps DESC_TEAMS
        desc_arg = 'DESC_TEAMS'

    # Personas — preserve original counts but cap at 3 (we now emit 3 prompts)
    def cap_persona(raw_kw):
        if not raw_kw: return None
        # raw_kw is a Python literal list — try to eval safely with limited names
        try:
            arr = eval(raw_kw, {'__builtins__': {}}, {})
            if isinstance(arr, list):
                if len(arr) >= 3:
                    return repr(arr[:3])
                # pad with last item
                while len(arr) < 3:
                    arr.append(arr[-1] if arr else 'Hadar Caspit')
                return repr(arr)
        except Exception:
            return raw_kw  # leave as-is
        return raw_kw

    persona_arg   = cap_persona(kw.get('persona'))
    personaID_arg = cap_persona(kw.get('personaID'))
    personaBM_arg = cap_persona(kw.get('personaBM'))

    indent_inner = indent + '  '

    out = ['tool(T_TEAMS, ' + lic_arg + ', ' + acct_arg + ', ',
           indent_inner + fmt_prompt_dicts(EN, indent_inner) + ', ' + desc_arg + ',',
           indent_inner + 'promptsID=' + fmt_prompt_dicts(ID, indent_inner) + ',',
           indent_inner + 'promptsBM=' + fmt_prompt_dicts(BM, indent_inner) + ',']
    if persona_arg:
        out.append(indent_inner + 'persona=' + persona_arg + ',')
    if personaID_arg:
        out.append(indent_inner + 'personaID=' + personaID_arg + ',')
    if personaBM_arg:
        out.append(indent_inner + 'personaBM=' + personaBM_arg + ',')
    # remove trailing comma on last line
    out[-1] = out[-1].rstrip(',')
    out.append(indent + ')')
    return '\n'.join(out)

# ── Run ────────────────────────────────────────────────────────────────────
files = sorted(glob.glob(os.path.join(ROOT, 'ind_batch*.py')) +
               glob.glob(os.path.join(ROOT, 'dept_data*.py')))
total = 0
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    blocks = find_team_blocks(src)
    if not blocks:
        continue
    # Replace right-to-left so offsets remain valid
    new_src = src
    for start, end in reversed(blocks):
        indent = get_indent(new_src, start)
        orig = new_src[start:end]
        replacement = build_new_call(orig, indent)
        new_src = replace_block(new_src, start, end, replacement)
        total += 1
    if new_src != src:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_src)
        print(f'  rewrote {len(blocks):>2} block(s) in {os.path.basename(path)}')

print(f'\nTotal blocks rewritten: {total}')

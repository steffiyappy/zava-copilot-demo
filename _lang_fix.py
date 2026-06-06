"""
_lang_fix.py — Post-build language correction pass.

Problem: many *BM fields contain Bahasa Indonesia text (some are exact copies of
*ID; others have BI words mixed into BM). Smaller problem in the reverse direction
on *ID fields.

Strategy: dictionary-based word-level substitution with case preservation and
proper-noun protection. Run as a post-build pass over data.js after build_master.py.

References:
  BM (Bahasa Malaysia) — Kamus DBP: https://kamus.dbp.gov.my/
  BI (Bahasa Indonesia) — KBBI: https://www.kbbi.web.id/

Word pairs are conservative — we only swap when the BI form is unambiguously
Indonesian (or BM form unambiguously Malay) AND the swap doesn't change meaning.
Proper nouns (Bursa Malaysia, OJK, BEI, KWSP, BPJS, etc.) are handled separately.
"""

# Bahasa Indonesia → Bahasa Malaysia (used to clean *BM fields)
# Conservative list — only words that are clearly BI-only and have a clear BM equivalent.
BI_TO_BM = [
    # Finance / business
    ('keuangan', 'kewangan'),
    ('perusahaan', 'syarikat'),
    ('bisnis', 'perniagaan'),
    ('rapat', 'mesyuarat'),
    ('karyawan', 'kakitangan'),
    ('pegawai', 'pegawai'),  # same — no-op, kept for documentation
    ('selisih', 'perbezaan'),
    ('biaya', 'kos'),
    ('hitung', 'kira'),
    ('menghitung', 'mengira'),
    ('dihitung', 'dikira'),
    ('perhitungan', 'pengiraan'),
    ('rupiah', 'ringgit'),
    ('pajak', 'cukai'),
    ('perpajakan', 'percukaian'),
    ('tunjangan', 'elaun'),
    ('berkas', 'fail'),
    ('kantor', 'pejabat'),
    ('propinsi', 'negeri'),
    ('provinsi', 'negeri'),
    ('anggota', 'ahli'),
    ('saja', 'sahaja'),
    ('silakan', 'sila'),
    ('bilang', 'sebut'),
    ('bilangan', 'bilangan'),  # same
    ('uang', 'wang'),
    ('senin', 'isnin'),
    ('kamis', 'khamis'),
    ('jumat', 'jumaat'),
    ('minggu', 'minggu'),  # ambiguous — leave (BM=Sunday, BI=week); skip
    # Government / institutions (Indonesian-specific terms swapped for Malaysian)
    ('pemerintah', 'kerajaan'),
    ('pemerintahan', 'pentadbiran'),
    ('direktur utama', 'pengarah urusan'),
    ('direktur', 'pengarah'),
    ('direksi', 'lembaga pengarah'),
    ('komisaris', 'pengerusi'),
    ('dewan komisaris', 'lembaga pengarah'),
    # Workflow / verbs
    ('membuat', 'membuat'),  # same
    ('membikin', 'membuat'),
    ('berubah', 'berubah'),  # same
    ('diubah', 'dipinda'),
    ('persetujuan', 'kelulusan'),
    ('menyetujui', 'meluluskan'),
    ('disetujui', 'diluluskan'),
    ('diperbarui', 'dikemaskini'),
    ('terbarui', 'terkini'),
    ('terbaru', 'terkini'),
    ('rapikan', 'kemaskan'),
    ('rapi', 'kemas'),
    # Time / sequence
    ('selesai', 'selesai'),  # same
    ('sebentar', 'sekejap'),
    ('sekarang', 'sekarang'),  # same
    ('besok', 'esok'),
    ('kemarin', 'semalam'),
    # Connectors / fillers
    ('karena', 'kerana'),
    ('makanya', 'maka'),
    # Common ID idioms not used in BM
    ('memerlukan', 'memerlukan'),  # same
    ('butuh', 'perlu'),
    ('membutuhkan', 'memerlukan'),
    # Indonesia-specific institutions → Malaysia equivalents
    # (Use case-insensitive matching with case preservation in the substitution)
    ('OJK', 'SC'),                 # Otoritas Jasa Keuangan → Suruhanjaya Sekuriti
    ('BEI', 'Bursa Malaysia'),     # Bursa Efek Indonesia → Bursa Malaysia
    ('IDX', 'Bursa Malaysia'),
    ('Bursa Efek Indonesia', 'Bursa Malaysia'),
    ('KSEI', 'Bursa Depository'),
    ('BPJS Kesehatan', 'PERKESO'),
    ('BPJS Ketenagakerjaan', 'KWSP'),
    ('BPJS', 'PERKESO'),
    ('DJP', 'LHDN'),
    ('Bank Indonesia', 'Bank Negara Malaysia'),
    ('BI ', 'BNM '),               # Trailing space to avoid catching word starts
    ('OJK', 'SC'),
    ('PSAK', 'MFRS'),              # Indonesian accounting standards → Malaysian
    ('RKAP', 'Belanjawan'),
    ('PT.', 'Sdn. Bhd.'),
    ('PT ', 'Sdn. Bhd. '),
    ('CV.', 'Sdn. Bhd.'),
    ('UU ', 'Akta '),
    ('Undang-Undang', 'Akta'),
    ('Indonesia', 'Malaysia'),     # Last — only when BM-tagged
]

# ── EXTRA pairs added 2026-06-06 after data.js translation audit ──────────
# Catches the remaining BI-only words that slipped past the original list.
# Format identical to BI_TO_BM above; appended to that list at module load.
_EXTRA_BI_TO_BM = [
    # Researcher instruction "Tempel prompt di bawah" — appeared 515× in BM
    ('Tempel', 'Tampal'), ('tempel', 'tampal'),
    ('Tempelnya', 'Tampalnya'), ('tempelnya', 'tampalnya'),
    # Management terminology
    ('manajer', 'pengurus'), ('Manajer', 'Pengurus'),
    ('manajemen', 'pengurusan'), ('Manajemen', 'Pengurusan'),
    ('mengelola', 'menguruskan'), ('Mengelola', 'Menguruskan'),
    ('dikelola', 'diuruskan'), ('Dikelola', 'Diuruskan'),
    ('pengelolaan', 'pengurusan'), ('Pengelolaan', 'Pengurusan'),
    ('pengelola', 'pengurus'), ('Pengelola', 'Pengurus'),
    # Expenditure / release
    ('pengeluaran', 'perbelanjaan'), ('Pengeluaran', 'Perbelanjaan'),
    ('merilis', 'mengeluarkan'), ('Merilis', 'Mengeluarkan'),
    ('dirilis', 'dikeluarkan'), ('Dirilis', 'Dikeluarkan'),
    ('rilis', 'siaran'), ('Rilis', 'Siaran'),
    # Schedule/plan
    ('jadwal', 'jadual'), ('Jadwal', 'Jadual'),
    ('jadwalnya', 'jadualnya'), ('Jadwalnya', 'Jadualnya'),
    ('jadwalkan', 'jadualkan'), ('Jadwalkan', 'Jadualkan'),
    ('menjadwalkan', 'menjadualkan'), ('Menjadwalkan', 'Menjadualkan'),
    ('penjadwalan', 'penjadualan'), ('Penjadwalan', 'Penjadualan'),
    ('terjadwal', 'berjadual'), ('Terjadwal', 'Berjadual'),
    # Account / accounting
    ('akun', 'akaun'), ('Akun', 'Akaun'),
    ('akunnya', 'akaunnya'), ('Akunnya', 'Akaunnya'),
    ('akuntabel', 'akauntabel'), ('Akuntabel', 'Akauntabel'),
    ('akuntabilitas', 'akauntabiliti'), ('Akuntabilitas', 'Akauntabiliti'),
    # Type / paste verbs (Researcher/Copilot UI)
    ('ketik', 'taip'), ('Ketik', 'Taip'),
    ('mengetik', 'menaip'), ('Mengetik', 'Menaip'),
    ('diketik', 'ditaip'), ('Diketik', 'Ditaip'),
    # Table → jadual (BM uses jadual for both schedule + table)
    ('tabel', 'jadual'), ('Tabel', 'Jadual'),
    ('tabelnya', 'jadualnya'), ('Tabelnya', 'Jadualnya'),
    # Phase / stage
    ('bertahap', 'berperingkat'), ('Bertahap', 'Berperingkat'),
    ('tahapan', 'peringkat'), ('Tahapan', 'Peringkat'),
    # Display
    ('menampilkan', 'memaparkan'), ('Menampilkan', 'Memaparkan'),
    ('tampilan', 'paparan'), ('Tampilan', 'Paparan'),
    ('tampilkan', 'paparkan'), ('Tampilkan', 'Paparkan'),
    ('ditampilkan', 'dipaparkan'), ('Ditampilkan', 'Dipaparkan'),
    # Upload / download
    ('unggah', 'muat naik'), ('Unggah', 'Muat naik'),
    ('mengunggah', 'memuat naik'), ('Mengunggah', 'Memuat naik'),
    ('diunggah', 'dimuat naik'), ('Diunggah', 'Dimuat naik'),
    ('unduh', 'muat turun'), ('Unduh', 'Muat turun'),
    ('mengunduh', 'memuat turun'), ('Mengunduh', 'Memuat turun'),
    ('diunduh', 'dimuat turun'), ('Diunduh', 'Dimuat turun'),
    # License / department
    ('lisensi', 'lesen'), ('Lisensi', 'Lesen'),
    ('berlisensi', 'berlesen'), ('Berlisensi', 'Berlesen'),
    ('departemen', 'jabatan'), ('Departemen', 'Jabatan'),
    ('departemennya', 'jabatannya'), ('Departemennya', 'Jabatannya'),
    # Differences
    ('perbedaan', 'perbezaan'), ('Perbedaan', 'Perbezaan'),
    ('berbeda', 'berbeza'), ('Berbeda', 'Berbeza'),
    ('membedakan', 'membezakan'), ('Membedakan', 'Membezakan'),
    # Subsidiary / parent company
    ('anak perusahaan', 'anak syarikat'), ('Anak perusahaan', 'Anak syarikat'),
    ('anak-anak perusahaan', 'anak-anak syarikat'),
    ('perusahaan induk', 'syarikat induk'), ('Perusahaan induk', 'Syarikat induk'),
    # Organize / hold (event)
    ('menyelenggarakan', 'menganjurkan'), ('Menyelenggarakan', 'Menganjurkan'),
    ('penyelenggaraan', 'penganjuran'), ('Penyelenggaraan', 'Penganjuran'),
    ('penyelenggara', 'penganjur'), ('Penyelenggara', 'Penganjur'),
    ('diselenggarakan', 'dianjurkan'), ('Diselenggarakan', 'Dianjurkan'),
    # Support
    ('mendukung', 'menyokong'), ('Mendukung', 'Menyokong'),
    ('didukung', 'disokong'), ('Didukung', 'Disokong'),
    ('pendukung', 'penyokong'), ('Pendukung', 'Penyokong'),
    ('dukungan', 'sokongan'), ('Dukungan', 'Sokongan'),
    # Suffixed forms of policy (kebijakan already in main list)
    ('kebijakannya', 'polisinya'), ('Kebijakannya', 'Polisinya'),
    # Suffixed kantor / berkas
    ('kantornya', 'pejabatnya'), ('Kantornya', 'Pejabatnya'),
    ('berkasnya', 'failnya'), ('Berkasnya', 'Failnya'),
    # Respond / react verbs
    ('menanggapi', 'membalas'), ('Menanggapi', 'Membalas'),
    ('tanggapan', 'jawapan'), ('Tanggapan', 'Jawapan'),
    ('ditanggapi', 'dibalas'), ('Ditanggapi', 'Dibalas'),
    ('menyikapi', 'menangani'), ('Menyikapi', 'Menangani'),
    # Try / attempt
    ('mencoba', 'mencuba'), ('Mencoba', 'Mencuba'),
    ('dicoba', 'dicuba'), ('Dicoba', 'Dicuba'),
    # Suffixed needs
    ('kebutuhan', 'keperluan'), ('Kebutuhan', 'Keperluan'),
    # Common file refs
    ('berkas-berkas', 'fail-fail'),
    # Indonesian-specific verbs
    ('memperbarui', 'mengemaskini'), ('Memperbarui', 'Mengemaskini'),
    ('pembaruan', 'kemaskini'), ('Pembaruan', 'Kemaskini'),
    # Currency abbrev (only useful if not preceded by "Rp" — risky; skip)
]

BI_TO_BM = BI_TO_BM + _EXTRA_BI_TO_BM

# Bahasa Malaysia → Bahasa Indonesia (used to clean *ID/BI fields)
BM_TO_BI = [
    ('kewangan', 'keuangan'),
    ('syarikat', 'perusahaan'),
    ('perniagaan', 'bisnis'),
    ('mesyuarat', 'rapat'),
    ('kakitangan', 'karyawan'),
    ('perbezaan', 'selisih'),
    ('kos', 'biaya'),
    ('kira', 'hitung'),
    ('mengira', 'menghitung'),
    ('dikira', 'dihitung'),
    ('pengiraan', 'perhitungan'),
    ('ringgit', 'rupiah'),
    ('cukai', 'pajak'),
    ('percukaian', 'perpajakan'),
    ('elaun', 'tunjangan'),
    ('fail', 'berkas'),
    ('pejabat', 'kantor'),
    ('negeri', 'provinsi'),
    ('ahli', 'anggota'),
    ('sahaja', 'saja'),
    ('sila', 'silakan'),
    ('wang', 'uang'),
    ('isnin', 'senin'),
    ('khamis', 'kamis'),
    ('jumaat', 'jumat'),
    ('kerajaan', 'pemerintah'),
    ('pentadbiran', 'pemerintahan'),
    ('pengarah urusan', 'direktur utama'),
    ('pengarah', 'direktur'),
    ('lembaga pengarah', 'direksi'),
    ('pengerusi', 'komisaris'),
    ('pengiraan', 'perhitungan'),
    ('dipinda', 'diubah'),
    ('kelulusan', 'persetujuan'),
    ('meluluskan', 'menyetujui'),
    ('diluluskan', 'disetujui'),
    ('dikemaskini', 'diperbarui'),
    ('terkini', 'terbaru'),
    ('kemaskan', 'rapikan'),
    ('kemas', 'rapi'),
    ('sekejap', 'sebentar'),
    ('esok', 'besok'),
    ('semalam', 'kemarin'),
    ('kerana', 'karena'),
    # Institutions: Malaysia → Indonesia
    ('SC ', 'OJK '),
    ('Suruhanjaya Sekuriti', 'OJK'),
    ('Bursa Malaysia', 'BEI'),
    ('PERKESO', 'BPJS'),
    ('KWSP', 'BPJS Ketenagakerjaan'),
    ('LHDN', 'DJP'),
    ('Bank Negara Malaysia', 'Bank Indonesia'),
    ('BNM ', 'BI '),
    ('MFRS', 'PSAK'),
    ('Belanjawan', 'RKAP'),
    ('Sdn. Bhd.', 'PT'),
    ('Sdn Bhd', 'PT'),
    ('Akta ', 'UU '),
    ('Malaysia', 'Indonesia'),     # Last
]

# ── EXTRA BM→BI pairs added 2026-06-06 (audit-driven) ─────────────────────
# Conservative — only words that are unambiguously BM-only AND have a clear
# BI equivalent. Excludes shared words like jabatan (BI: position/post),
# paparan (BI: exposure), perlu, boleh — the audit confirmed those appear
# legitimately in BI text and must NOT be swapped.
_EXTRA_BM_TO_BI = [
    ('Tampal', 'Tempel'), ('tampal', 'tempel'),
    ('jadual', 'jadwal'), ('Jadual', 'Jadwal'),
    ('jadualkan', 'jadwalkan'), ('Jadualkan', 'Jadwalkan'),
    ('menjadualkan', 'menjadwalkan'), ('Menjadualkan', 'Menjadwalkan'),
    ('akaun', 'akun'), ('Akaun', 'Akun'),
    ('akauntabel', 'akuntabel'), ('Akauntabel', 'Akuntabel'),
    ('akauntabiliti', 'akuntabilitas'), ('Akauntabiliti', 'Akuntabilitas'),
    ('taip', 'ketik'), ('Taip', 'Ketik'),
    ('menaip', 'mengetik'), ('Menaip', 'Mengetik'),
    ('muat naik', 'unggah'), ('Muat naik', 'Unggah'),
    ('memuat naik', 'mengunggah'), ('Memuat naik', 'Mengunggah'),
    ('muat turun', 'unduh'), ('Muat turun', 'Unduh'),
    ('memuat turun', 'mengunduh'), ('Memuat turun', 'Mengunduh'),
    ('lesen', 'lisensi'), ('Lesen', 'Lisensi'),
    ('berlesen', 'berlisensi'), ('Berlesen', 'Berlisensi'),
    ('perbezaan', 'perbedaan'), ('Perbezaan', 'Perbedaan'),
    ('berbeza', 'berbeda'), ('Berbeza', 'Berbeda'),
    ('anak syarikat', 'anak perusahaan'), ('Anak syarikat', 'Anak perusahaan'),
    ('syarikat induk', 'perusahaan induk'), ('Syarikat induk', 'Perusahaan induk'),
    ('menyokong', 'mendukung'), ('Menyokong', 'Mendukung'),
    ('disokong', 'didukung'), ('Disokong', 'Didukung'),
    ('penyokong', 'pendukung'), ('Penyokong', 'Pendukung'),
    ('sokongan', 'dukungan'), ('Sokongan', 'Dukungan'),
    ('mencuba', 'mencoba'), ('Mencuba', 'Mencoba'),
    ('keperluan', 'kebutuhan'), ('Keperluan', 'Kebutuhan'),
    ('mengemaskini', 'memperbarui'), ('Mengemaskini', 'Memperbarui'),
    ('dikemaskini', 'diperbarui'), ('Dikemaskini', 'Diperbarui'),
]

BM_TO_BI = BM_TO_BI + _EXTRA_BM_TO_BI


def _apply_subs(text, subs):
    """Apply substitutions with word-boundary matching and case preservation."""
    if not text or not isinstance(text, str):
        return text
    import re
    out = text
    for src, dst in subs:
        if not src:
            continue
        if src.endswith(' '):
            # Phrase substitution — anchor with word boundary at start to avoid
            # matching inside other words (e.g. "PT " must not match "promPT ").
            pattern = r'\b' + re.escape(src.rstrip(' ')) + r' '
            replacement = dst
            out = re.sub(pattern, replacement, out, flags=re.IGNORECASE)
        else:
            # Word-boundary match, case-insensitive, preserve case of each word.
            pattern = r'\b' + re.escape(src) + r'\b'

            def _repl(m, _src=src, _dst=dst):
                orig = m.group(0)
                # All-uppercase short codes (OJK, BEI, RKAP) → upper-case dst
                if orig.isupper() and len(orig) > 1 and len(_src.split()) == 1:
                    return _dst.upper()
                # Multi-word: preserve title-case per word
                if ' ' in _dst and ' ' in orig:
                    src_words = orig.split()
                    dst_words = _dst.split()
                    return ' '.join(
                        (dw[0].upper() + dw[1:]) if (i < len(src_words) and src_words[i][:1].isupper()) else dw
                        for i, dw in enumerate(dst_words)
                    )
                # Multi-word dst, single-word original: title-case if original was capitalized
                if ' ' in _dst and orig[:1].isupper():
                    return ' '.join((w[0].upper() + w[1:]) if w else w for w in _dst.split())
                # Single word: capitalise first letter if original was
                if orig[:1].isupper() and _dst:
                    return _dst[0].upper() + _dst[1:]
                return _dst

            out = re.sub(pattern, _repl, out, flags=re.IGNORECASE)
    return out


def fix_bm(text):
    """Fix a *BM-tagged field: apply BI→BM substitutions."""
    return _apply_subs(text, BI_TO_BM)


def fix_bi(text):
    """Fix a *ID/BI-tagged field: apply BM→BI substitutions."""
    return _apply_subs(text, BM_TO_BI)


def walk_and_fix(entry):
    """Walk an entry and fix all *BM and *ID/*BI fields in place. Returns count of fixes."""
    fixes = 0

    def patch(obj, key, fixer):
        nonlocal fixes
        if key not in obj:
            return
        v = obj[key]
        if isinstance(v, str):
            new = fixer(v)
            if new != v:
                obj[key] = new
                fixes += 1
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, str):
                    new = fixer(item)
                    if new != item:
                        v[i] = new
                        fixes += 1
                elif isinstance(item, dict):
                    for sub in ('prompt', 'instr', 'text', 'label', 'title', 'desc'):
                        if sub in item and isinstance(item[sub], str):
                            new = fixer(item[sub])
                            if new != item[sub]:
                                item[sub] = new
                                fixes += 1

    # Top-level entry fields
    for fn in ('name', 'company', 'tagline', 'scenario'):
        for suf, fixer in (('BM', fix_bm), ('ID', fix_bi)):
            patch(entry, fn + suf, fixer)

    # Tool prompts
    for t in entry.get('prompts', []) or []:
        patch(t, 'promptsBM', fix_bm)
        patch(t, 'promptsID', fix_bi)
        patch(t, 'personaBM', fix_bm)
        patch(t, 'personaID', fix_bi)
        # agentsBM/agentsID on the tool itself (tool_builder_free puts them here).
        # build_master line 988: agentsBM=agents_id (copy of ID text), so BM agents
        # arrive as raw BI and need dialect cleanup.
        for agents_key, fixer in (('agentsBM', fix_bm), ('agentsID', fix_bi)):
            for ag in t.get(agents_key, []) or []:
                if not isinstance(ag, dict):
                    continue
                for sub in ('label', 'name', 'desc', 'instructions', 'knowledgeNote'):
                    if sub in ag and isinstance(ag[sub], str):
                        new = fixer(ag[sub])
                        if new != ag[sub]:
                            ag[sub] = new
                            fixes += 1
                qs = ag.get('queries') or []
                if isinstance(qs, list):
                    for i, q in enumerate(qs):
                        if isinstance(q, str):
                            new = fixer(q)
                            if new != q:
                                qs[i] = new
                                fixes += 1
                ks = ag.get('knowledge') or []
                if isinstance(ks, list):
                    for k in ks:
                        if isinstance(k, dict) and isinstance(k.get('note'), str):
                            new = fixer(k['note'])
                            if new != k['note']:
                                k['note'] = new
                                fixes += 1

    # Storyboard
    for ch in entry.get('storyboard', []) or []:
        patch(ch, 'titleBM', fix_bm)
        patch(ch, 'titleID', fix_bi)
        patch(ch, 'summaryBM', fix_bm)
        patch(ch, 'summaryID', fix_bi)
        for tk in ch.get('tasks', []) or []:
            patch(tk, 'verbBM', fix_bm)
            patch(tk, 'verbID', fix_bi)

    # Personas
    for p in entry.get('personas', []) or []:
        patch(p, 'roleBM', fix_bm)
        patch(p, 'roleID', fix_bi)

    # Sharing / immersion library extras (descBM/ID, leadsBM/ID, objectiveBM/ID,
    # exerciseBM/ID, taskBM/ID, licenseBM/ID, instructionsBM/ID).
    for suf, fixer in (('BM', fix_bm), ('ID', fix_bi)):
        for fn in ('desc', 'license', 'instructions', 'objective'):
            patch(entry, fn + suf, fixer)
        for list_field in ('leads', 'exercise', 'task'):
            patch(entry, list_field + suf, fixer)

    return fixes


if __name__ == '__main__':
    # Quick smoke test
    sample_bi = "Direktur Utama memerlukan naskah pembukaan untuk Mesyuarat Direksi pasca selisih EBITDA 18% di konglomerat dengan 8.400 karyawan dan biaya operasional naik. RKAP FY2025 disetujui OJK."
    print("BI input:", sample_bi)
    print("BM fixed:", fix_bm(sample_bi))

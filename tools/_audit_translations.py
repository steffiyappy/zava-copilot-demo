"""Audit translation quality across data.js.

Walks the in-memory entry tree (re-imports build_master path) and scans every
promptsBM / promptsID / promptsBM-tagged field for known wrong-language words.
Reports counts + sample contexts.

Usage:
  python tools/_audit_translations.py
"""
import sys, re, json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Words that should NOT appear in Bahasa Malaysia text (they are BI-only).
# We exclude entity names (PT, OJK, etc.) and ambiguous shared words.
BI_ONLY_IN_BM = [
    'perusahaan', 'keuangan', 'bisnis', 'rapat', 'karyawan', 'biaya', 'biayanya',
    'menghitung', 'dihitung', 'perhitungan', 'pajak', 'perpajakan', 'tunjangan',
    'berkas', 'kantor', 'provinsi', 'propinsi', 'silakan', 'sekarang juga',
    'kamis', 'jumat', 'pemerintah', 'pemerintahan', 'direktur utama', 'direktur',
    'direksi', 'komisaris', 'persetujuan', 'menyetujui', 'disetujui',
    'diperbarui', 'terbaru', 'butuh ', 'membutuhkan', 'kebijakan', 'kebijakannya',
    'memutuskan', 'putusan',
    # Mining/legal/business specific BI words
    'jadwal', 'menjadwalkan', 'penjadwalan', 'tabel', 'tabelnya', 'tahap',
    'tahapan', 'mengelola', 'pengelolaan', 'manajer', 'memproses', 'merilis',
    'rilis', 'mengirim', 'pengiriman', 'memesan', 'pesanan',
    'menggunakan',  # actually OK in BM too — REMOVE
    'menyiapkan', 'penyiapan', 'menyajikan', 'menyerahkan', 'penyerahan',
    'mengeluarkan', 'pengeluaran', 'pengeluarannya',
    'anak perusahaan', 'perusahaan induk',
    'pegawai negeri', 'aparatur',
    'memberikan', 'pemberian',  # ambiguous - shared usage
    'pengakuan', 'mengakui',
    'menyelenggarakan', 'penyelenggaraan',
    'sehingga', 'agar', 'supaya',  # shared - REMOVE
    'menyebabkan',
    'menanggapi', 'menyikapi',
    'menambahkan',  # shared
    'mempengaruhi', 'pengaruh',  # shared
    'mendiskusikan', 'diskusi',  # shared
    # Heavily BI vocab
    'dampak', 'berdampak',  # ambiguous
    'tetapi', 'namun',  # shared
    'lebih lanjut', 'selanjutnya',
    'sangat penting', 'paling penting',
    'kondisi', 'kondisinya',  # shared
    # Files/IT
    'perintah', 'mengirim e-mail',
    # Indonesia-only verbs/nouns
    'dapat', 'tidak dapat',  # shared
    'menerima', 'penerimaan',  # shared
    'memberi tahu', 'pemberitahuan',
    'mengusulkan', 'usulan', 'usul',
    'membicarakan', 'pembicaraan',
    'menetapkan', 'penetapan',  # shared
    'kepala bagian',
    'dengan demikian',
]

# Trim to highest-signal subset (avoid false positives)
BI_ONLY_IN_BM = [
    'perusahaan', 'keuangan', 'bisnis ', 'rapat ', ' rapat', 'karyawan',
    'biaya', 'menghitung', 'dihitung', 'perhitungan', 'pajak', 'perpajakan',
    'tunjangan', 'berkas', 'kantor', 'provinsi', 'silakan', 'kamis ',
    'jumat ', 'pemerintah', 'pemerintahan', 'direktur', 'direksi', 'komisaris',
    'persetujuan', 'menyetujui', 'disetujui', 'diperbarui', 'terbaru',
    'membutuhkan', 'kebijakan', 'jadwal', 'tabel',
    'tahapan', 'mengelola', 'pengelolaan', 'manajer',
    'menanggapi', 'menyikapi', 'mendukung', 'pendukung', 'didukung',
    'merilis', 'rilis',
    'akun',
    'tampilan', 'menampilkan', 'tampilkan',
    'unggah', 'mengunggah', 'unduh', 'mengunduh',
    'lisensi', 'berlisensi',
    'departemen',
    'perbedaan', 'berbeda',
    'butuh',
    'ketik', 'mengetik',
    'tempel', 'tempelkan',
]

# Words that should NOT appear in Bahasa Indonesia text (BM-only).
# Stripped of false positives (perlu, boleh, jabatan are shared in BI too;
# kos/esok/fail/pengarah are substring-prone).
BM_ONLY_IN_BI = [
    'syarikat', 'kewangan', 'perniagaan', 'mesyuarat', 'kakitangan',
    'mengira', 'dikira', 'pengiraan', 'cukai', 'percukaian', 'elaun',
    'pejabat', 'sahaja', 'wang ',
    'isnin', 'khamis', 'jumaat', 'kerajaan', 'pentadbiran',
    'pengarah urusan', 'lembaga pengarah', 'pengerusi', 'kelulusan',
    'meluluskan', 'diluluskan', 'dikemaskini', 'sekejap',
    'kerana', 'jadual', 'menjadualkan',
    'menyokong', 'sokongan', 'akaun', 'taip', 'menaip',
    'tampal', 'tampalkan',
    'lesen', 'berlesen',
    'perbezaan', 'berbeza',
    'syarikat induk', 'anak syarikat',
    'jenama',
]


def extract_arrays(data_text, key):
    """Yield (start_offset, [str_items]) tuples for every  key:[ ... ] block."""
    pattern = re.compile(r'\b' + re.escape(key) + r':\s*\[')
    for m in pattern.finditer(data_text):
        start = m.end()
        depth = 1
        i = start
        while i < len(data_text) and depth > 0:
            ch = data_text[i]
            if ch == '[':
                depth += 1
            elif ch == ']':
                depth -= 1
                if depth == 0:
                    break
            elif ch == "'":
                j = i + 1
                while j < len(data_text):
                    if data_text[j] == '\\':
                        j += 2
                        continue
                    if data_text[j] == "'":
                        break
                    j += 1
                i = j
            elif ch == '"':
                j = i + 1
                while j < len(data_text):
                    if data_text[j] == '\\':
                        j += 2
                        continue
                    if data_text[j] == '"':
                        break
                    j += 1
                i = j
            i += 1
        body = data_text[start:i]
        # Pull all single-quoted strings (data.js uses single quotes)
        strings = re.findall(r"'((?:[^'\\]|\\.)*)'", body)
        yield m.start(), strings


def audit(data_text, key, bad_words, label):
    print(f'\n══ {label} (field={key}) ══')
    word_hits = defaultdict(int)
    sample_per_word = {}
    total_strings = 0
    for offset, strings in extract_arrays(data_text, key):
        for s in strings:
            total_strings += 1
            for w in bad_words:
                # Word-boundary match (avoids kosong→kos, besok→esok, fails→fail)
                pat = r'\b' + re.escape(w) + r'\b'
                for m in re.finditer(pat, s, re.IGNORECASE):
                    word_hits[w] += 1
                    if w not in sample_per_word:
                        idx = m.start()
                        ctx = s[max(0, idx - 40):idx + len(w) + 40]
                        sample_per_word[w] = ctx
                    break  # count once per string
    print(f'  Strings scanned: {total_strings}')
    if not word_hits:
        print('  ✓ No issues found.')
        return 0
    print(f'  Words found in wrong-language fields:')
    for w, c in sorted(word_hits.items(), key=lambda x: -x[1])[:40]:
        sample = sample_per_word.get(w, '')[:120].replace('\n', ' ')
        print(f'    {c:5d}  {w:25s}  ↳ {sample}…')
    return sum(word_hits.values())


if __name__ == '__main__':
    data = (ROOT / 'data.js').read_text(encoding='utf-8')
    print(f'data.js loaded: {len(data):,} bytes')

    bm_issues = audit(data, 'promptsBM', BI_ONLY_IN_BM,
                      'BI-only words appearing in promptsBM (should be BM)')
    bi_issues = audit(data, 'promptsID', BM_ONLY_IN_BI,
                      'BM-only words appearing in promptsID (should be BI)')

    print(f'\n══ TOTAL: BM issues={bm_issues}, BI issues={bi_issues} ══')

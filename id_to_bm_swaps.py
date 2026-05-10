"""
ID -> BM token swaps applied at build time so MY_BM users see consistent
Bahasa Malaysia rather than the half-EN / half-BM mix they used to get when
~93% of promptsBM arrays were empty and the renderer fell back to English.

Strategy: every empty `promptsBM` is filled by cloning the matching
`promptsID` then running the strings through `id_to_bm` to swap the
high-frequency ID-only tokens for their BM equivalents. Bahasa Malaysia and
Bahasa Indonesia are ~80% mutually intelligible so this gives a result that
reads as natural BM with a slight Indonesian flavour — vastly better than
English fallback.

Anything that's the same in both languages (klik, pilih, buka, agen, agenda,
audit, prompt, tools, …) is *intentionally* not in the map.
"""

import re

# Ordered list (longer / multi-word phrases FIRST so they match before the
# single-word swaps below would have a chance to bite half of them).
_ID_TO_BM_PAIRS = [
    # multi-word first
    ('Secara otomatis', 'Secara automatik'),
    ('secara otomatis', 'secara automatik'),
    ('tidak terbatas', 'tidak terhad'),
    ('Tidak terbatas', 'Tidak terhad'),
    ('Pemegang Saham', 'Pemegang Saham'),  # same; kept as a no-swap anchor

    # single-word swaps (paired by case)
    ('Ketik', 'Taip'), ('ketik', 'taip'),
    ('Mengetik', 'Menaip'), ('mengetik', 'menaip'),
    ('Tempelkan', 'Tampalkan'), ('tempelkan', 'tampalkan'),
    ('Menempelkan', 'Menampalkan'), ('menempelkan', 'menampalkan'),
    ('Unggah', 'Muat naik'), ('unggah', 'muat naik'),
    ('Mengunggah', 'Memuat naik'), ('mengunggah', 'memuat naik'),
    ('Diunggah', 'Dimuat naik'), ('diunggah', 'dimuat naik'),
    ('Unduh', 'Muat turun'), ('unduh', 'muat turun'),
    ('Mengunduh', 'Memuat turun'), ('mengunduh', 'memuat turun'),
    ('Diunduh', 'Dimuat turun'), ('diunduh', 'dimuat turun'),
    ('Akun', 'Akaun'), ('akun', 'akaun'),
    ('Lisensi', 'Lesen'), ('lisensi', 'lesen'),
    ('Berlisensi', 'Berlesen'), ('berlisensi', 'berlesen'),
    ('Perusahaan', 'Syarikat'), ('perusahaan', 'syarikat'),
    ('Kantor', 'Pejabat'), ('kantor', 'pejabat'),
    ('Anggaran', 'Belanjawan'), ('anggaran', 'belanjawan'),
    ('Departemen', 'Jabatan'), ('departemen', 'jabatan'),
    ('Tampilan', 'Paparan'), ('tampilan', 'paparan'),
    ('Menampilkan', 'Memaparkan'), ('menampilkan', 'memaparkan'),
    ('Tampilkan', 'Paparkan'), ('tampilkan', 'paparkan'),
    ('Ditampilkan', 'Dipaparkan'), ('ditampilkan', 'dipaparkan'),
    ('Perbedaan', 'Perbezaan'), ('perbedaan', 'perbezaan'),
    ('Berbeda', 'Berbeza'), ('berbeda', 'berbeza'),
    ('Selesai', 'Siap'), ('selesai', 'siap'),
    ('Menyelesaikan', 'Menyiapkan'), ('menyelesaikan', 'menyiapkan'),
    ('Diselesaikan', 'Disiapkan'), ('diselesaikan', 'disiapkan'),
    ('Harus', 'Perlu'), ('harus', 'perlu'),
    ('Seharusnya', 'Sepatutnya'), ('seharusnya', 'sepatutnya'),
    ('Kebijakan', 'Polisi'), ('kebijakan', 'polisi'),
    ('Bijak', 'Bijak'),  # same anchor
    ('Bisa', 'Boleh'), ('bisa', 'boleh'),
    ('Kalian', 'Anda'), ('kalian', 'anda'),
    ('Kamu', 'Anda'), ('kamu', 'anda'),
    ('Diskon', 'Diskaun'), ('diskon', 'diskaun'),
    ('Evaluasi', 'Penilaian'), ('evaluasi', 'penilaian'),
    ('Mengevaluasi', 'Menilai'), ('mengevaluasi', 'menilai'),
    ('Dievaluasi', 'Dinilai'), ('dievaluasi', 'dinilai'),
    ('Memungkinkan', 'Membolehkan'), ('memungkinkan', 'membolehkan'),
    ('Dimungkinkan', 'Dibolehkan'), ('dimungkinkan', 'dibolehkan'),
    ('Rincian', 'Perincian'), ('rincian', 'perincian'),
    ('Rinci', 'Terperinci'), ('rinci', 'terperinci'),
    ('Tipe', 'Jenis'), ('tipe', 'jenis'),
    ('Selanjutnya', 'Seterusnya'), ('selanjutnya', 'seterusnya'),
    ('Terbaru', 'Terkini'), ('terbaru', 'terkini'),
    ('Tabel', 'Jadual'), ('tabel', 'jadual'),
    ('Ekspor', 'Eksport'), ('ekspor', 'eksport'),
    ('Mengekspor', 'Mengeksport'), ('mengekspor', 'mengeksport'),
    ('Diekspor', 'Dieksport'), ('diekspor', 'dieksport'),
    ('Impor', 'Import'), ('impor', 'import'),
    ('Mengimpor', 'Mengimport'), ('mengimpor', 'mengimport'),
    ('Diimpor', 'Diimport'), ('diimpor', 'diimport'),
    ('Rapat', 'Mesyuarat'), ('rapat', 'mesyuarat'),
    ('Jadwal', 'Jadual'), ('jadwal', 'jadual'),
    ('Menjadwalkan', 'Menjadualkan'), ('menjadwalkan', 'menjadualkan'),
    ('Dijadwalkan', 'Dijadualkan'), ('dijadwalkan', 'dijadualkan'),
    ('Penjualan', 'Jualan'), ('penjualan', 'jualan'),
    ('Kontrol', 'Kawalan'), ('kontrol', 'kawalan'),
    ('Mengontrol', 'Mengawal'), ('mengontrol', 'mengawal'),
    ('Lembar', 'Helaian'), ('lembar', 'helaian'),
    ('Lembaran', 'Helaian'), ('lembaran', 'helaian'),
    ('Kapan', 'Bila'), ('kapan', 'bila'),
    ('Yaitu', 'Iaitu'), ('yaitu', 'iaitu'),
    ('Minimal', 'Minimum'), ('minimal', 'minimum'),
    ('Maksimal', 'Maksimum'), ('maksimal', 'maksimum'),
    ('Didukung', 'Disokong'), ('didukung', 'disokong'),
    ('Mendukung', 'Menyokong'), ('mendukung', 'menyokong'),
    ('Pendukung', 'Penyokong'), ('pendukung', 'penyokong'),
    ('Mendeskripsikan', 'Menerangkan'), ('mendeskripsikan', 'menerangkan'),
    ('Deskripsi', 'Penerangan'), ('deskripsi', 'penerangan'),
    ('Otomatis', 'Automatik'), ('otomatis', 'automatik'),
    ('Resmi', 'Rasmi'), ('resmi', 'rasmi'),
    ('Kolom', 'Lajur'), ('kolom', 'lajur'),
    ('File', 'Fail'), ('file', 'fail'),
    ('Berkas', 'Fail'), ('berkas', 'fail'),
    ('Rekomendasi', 'Cadangan'), ('rekomendasi', 'cadangan'),
    ('Merekomendasikan', 'Mengesyorkan'), ('merekomendasikan', 'mengesyorkan'),
    ('Direkomendasikan', 'Disyorkan'), ('direkomendasikan', 'disyorkan'),
    ('Mengembangkan', 'Membangunkan'), ('mengembangkan', 'membangunkan'),
    ('Dikembangkan', 'Dibangunkan'), ('dikembangkan', 'dibangunkan'),
    ('Pengembangan', 'Pembangunan'), ('pengembangan', 'pembangunan'),
    ('Siapkan', 'Sediakan'), ('siapkan', 'sediakan'),
    ('Menyiapkan', 'Menyediakan'), ('menyiapkan', 'menyediakan'),
    ('Disiapkan', 'Disediakan'), ('disiapkan', 'disediakan'),
    ('Dibutuhkan', 'Diperlukan'), ('dibutuhkan', 'diperlukan'),
    ('Membutuhkan', 'Memerlukan'), ('membutuhkan', 'memerlukan'),
    ('Kebutuhan', 'Keperluan'), ('kebutuhan', 'keperluan'),
    ('Butuh', 'Perlu'), ('butuh', 'perlu'),
    ('Mengirim', 'Menghantar'), ('mengirim', 'menghantar'),
    ('Mengirimkan', 'Menghantar'), ('mengirimkan', 'menghantar'),
    ('Kirim', 'Hantar'), ('kirim', 'hantar'),
    ('Dikirim', 'Dihantar'), ('dikirim', 'dihantar'),
    ('Dikirimkan', 'Dihantar'), ('dikirimkan', 'dihantar'),
    ('Mengundang', 'Menjemput'), ('mengundang', 'menjemput'),
    ('Undangan', 'Jemputan'), ('undangan', 'jemputan'),
    ('Diundang', 'Dijemput'), ('diundang', 'dijemput'),
    ('Mencakup', 'Merangkumi'), ('mencakup', 'merangkumi'),
    ('Mencakupi', 'Merangkumi'), ('mencakupi', 'merangkumi'),
    ('Merek', 'Jenama'), ('merek', 'jenama'),
    ('Merk', 'Jenama'), ('merk', 'jenama'),
    ('Ukuran', 'Saiz'), ('ukuran', 'saiz'),
    ('Temukan', 'Cari'), ('temukan', 'cari'),
    ('Menemukan', 'Mencari'), ('menemukan', 'mencari'),
    ('Ditemukan', 'Dicari'), ('ditemukan', 'dicari'),  # close-enough
    ('Izin', 'Kebenaran'), ('izin', 'kebenaran'),
    ('Mengizinkan', 'Membenarkan'), ('mengizinkan', 'membenarkan'),
    ('Diizinkan', 'Dibenarkan'), ('diizinkan', 'dibenarkan'),
    ('Diagram', 'Rajah'), ('diagram', 'rajah'),
    ('Waktu', 'Masa'), ('waktu', 'masa'),
    ('Jaringan', 'Rangkaian'), ('jaringan', 'rangkaian'),
    ('Administrator', 'Pentadbir'), ('administrator', 'pentadbir'),
    ('Ikhtisar', 'Ringkasan'), ('ikhtisar', 'ringkasan'),
    ('Kerjakan', 'Lakukan'), ('kerjakan', 'lakukan'),
    ('Mengerjakan', 'Melakukan'), ('mengerjakan', 'melakukan'),
    ('Dikerjakan', 'Dilakukan'), ('dikerjakan', 'dilakukan'),
    ('Foto', 'Gambar'), ('foto', 'gambar'),
    ('Mobil', 'Kereta'), ('mobil', 'kereta'),
    ('Sepeda', 'Basikal'), ('sepeda', 'basikal'),
    ('Stasiun', 'Stesen'), ('stasiun', 'stesen'),
    ('Apotek', 'Farmasi'), ('apotek', 'farmasi'),
    ('Apotik', 'Farmasi'), ('apotik', 'farmasi'),
    ('Operasi', 'Operasi'),  # same
    ('Dokter', 'Doktor'), ('dokter', 'doktor'),
    ('Susulan', 'Susulan'),  # same
    ('Sektor', 'Sektor'),  # same
    ('Sebagaimana', 'Sebagaimana'),  # same
    ('Selalu', 'Sentiasa'), ('selalu', 'sentiasa'),
    ('Hanya', 'Hanya'),  # same
    ('Bermanfaat', 'Berfaedah'), ('bermanfaat', 'berfaedah'),
    ('Manfaat', 'Faedah'), ('manfaat', 'faedah'),
    ('Memanfaatkan', 'Memanfaatkan'),  # same
    ('Sepenuhnya', 'Sepenuhnya'),  # same
    ('Sebagian', 'Sebahagian'), ('sebagian', 'sebahagian'),
    ('Sebagian besar', 'Sebahagian besar'),
    ('Bagian', 'Bahagian'), ('bagian', 'bahagian'),
    ('Berbagi', 'Berkongsi'), ('berbagi', 'berkongsi'),
    ('Membagi', 'Membahagi'), ('membagi', 'membahagi'),
    ('Dibagi', 'Dibahagi'), ('dibagi', 'dibahagi'),
    ('Pembagian', 'Pembahagian'), ('pembagian', 'pembahagian'),
    ('Mungkin', 'Mungkin'),  # same
    ('Memang', 'Memang'),  # same
    ('Kondisi', 'Keadaan'), ('kondisi', 'keadaan'),
    ('Situasi', 'Situasi'),  # same
    ('Posisi', 'Kedudukan'), ('posisi', 'kedudukan'),
    ('Pertama', 'Pertama'),  # same
    ('Kedua', 'Kedua'),  # same
    ('Ketiga', 'Ketiga'),  # same
    ('Keempat', 'Keempat'),  # same
    ('Kelima', 'Kelima'),  # same
    ('Keenam', 'Keenam'),  # same
    ('Setiap', 'Setiap'),  # same
    ('Setiap hari', 'Setiap hari'),  # same
    ('Setiap minggu', 'Setiap minggu'),  # same
    ('Bulan', 'Bulan'),  # same
    ('Tahun', 'Tahun'),  # same
    ('Hari', 'Hari'),  # same
    ('Negeri', 'Negeri'),  # same
    ('Negara', 'Negara'),  # same
    ('Tetap', 'Tetap'),  # same
    ('Penanda', 'Penanda'),  # same
    ('Penyimpan', 'Penyimpan'),  # same
    ('Penyimpanan', 'Penyimpanan'),  # same
    ('Mencari', 'Mencari'),  # same
    ('Pencarian', 'Carian'), ('pencarian', 'carian'),
]


_compiled = None


def _compile():
    """Compile a single combined regex for performance."""
    global _compiled
    if _compiled is not None:
        return
    # Sort longer patterns first so multi-word swaps win
    pairs = sorted(_ID_TO_BM_PAIRS, key=lambda p: -len(p[0]))
    parts = []
    table = {}
    for src, dst in pairs:
        # Skip identical pairs (no-op anchors): they only exist to keep the list
        # readable; they don't need to be in the regex.
        if src == dst:
            continue
        parts.append(re.escape(src))
        table[src] = dst
    pattern = r'(?<![A-Za-z])(' + '|'.join(parts) + r')(?![A-Za-z])'
    _compiled = (re.compile(pattern), table)


def id_to_bm(s):
    if not isinstance(s, str) or not s:
        return s
    _compile()
    rx, table = _compiled
    def _sub(m):
        return table.get(m.group(0), m.group(0))
    return rx.sub(_sub, s)


def clone_id_prompts_to_bm(prompts_id):
    """Clone a promptsID list into a promptsBM list with token swaps applied."""
    if not prompts_id:
        return []
    out = []
    for p in prompts_id:
        if isinstance(p, str):
            out.append(id_to_bm(p))
        elif isinstance(p, dict):
            r = dict(p)
            for k in ('instr', 'prompt', 'note', 'desc', 'label', 'instructions'):
                if k in r and isinstance(r[k], str):
                    r[k] = id_to_bm(r[k])
            out.append(r)
        else:
            out.append(p)
    return out


def fill_missing_bm_from_id(entries):
    """Walk entries (industries or departments) and fill empty promptsBM
    from non-empty promptsID with token swaps. Returns count of tools filled."""
    filled = 0
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        tools = entry.get('prompts')
        if not isinstance(tools, list):
            continue
        for tool in tools:
            if not isinstance(tool, dict):
                continue
            bm = tool.get('promptsBM')
            idd = tool.get('promptsID')
            if (not bm) and idd:
                tool['promptsBM'] = clone_id_prompts_to_bm(idd)
                filled += 1
    return filled

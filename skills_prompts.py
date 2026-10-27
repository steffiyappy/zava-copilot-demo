# -*- coding: utf-8 -*-
"""Skills prompts (27 Oct 2026).

Appends skills-focused prompts to the Copilot in Excel and Copilot in PowerPoint
blocks of every industry and department entry, in English, Bahasa Malaysia and
Bahasa Indonesia. (Cowork skills live in the Cowork Library, see _cowork_library.py.) Each prompt is filled from the entry's own name, sample
workbooks and tagline, so the demo runs on files the entry already ships.

Sources (Microsoft Support and Microsoft Learn, checked 27 Oct 2026):
  Excel skills        https://support.microsoft.com/en-us/excel/copilot/copilot-in-excel-skills
  Excel built-ins     https://support.microsoft.com/en-us/excel/copilot/copilot-in-excel-built-in-skills
  Cowork skills       https://learn.microsoft.com/en-us/copilot/cowork/cowork-customize
  PowerPoint skills   https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

Runs after the BM/BI dialect cleanup, so the Bahasa text below is written in the
final dialect and is not rewritten again.
"""
import re

_SKIP_XLSX = re.compile(r'^(Scout_|Autopilot_|Heartbeat_|00_Copilot)', re.I)

# One entry per prompt: instr (how to start) and prompt (what to paste).
T = {
    'EN': {
        'xl1': {
            'instr': "Open the workbook in Excel for the web and open the **Copilot pane**. In the prompt box select **Add** > **Choose plugins and skills**, or type `@` and pick a skill. `@clean-data` is rolling out in stages, so it may not be on every tenant yet.",
            'prompt': "@clean-data Inspect {xlsx} for issues that can break formulas, lookups, PivotTables and reports: extra spaces, inconsistent text and number formats, inconsistent dates, duplicate values and values stored as the wrong data type. Explain what you found and why it matters for {name}, then propose corrections and let me choose which changes to apply.",
        },
        'xl2': {
            'instr': "Stay in the same Copilot pane. Type `@skill-builder` and describe the skill. Copilot shows a preview that you can refine before it saves the skill to your OneDrive skills folder. `@skill-builder` is rolling out in stages, so it may not be on every tenant yet.",
            'prompt': "@skill-builder Create a skill named {skill}-monthly-review for the {name} team. When I ask for the monthly review, it should open {xlsx}, format the main table, highlight negative variances in red, add a summary chart and write a three-line commentary that ends with one recommended action. {ctx}Show me a preview before you save it.",
        },
        'xl3': {
            'instr': "Do this after you finish a multi-step task with Copilot in the same chat, for example the previous prompt. Copilot captures the steps, the decision rules and the expected output, and shows a preview before it saves.",
            'prompt': "Save what we just did to a new skill named {skill}-quarterly-pack. Capture the steps, the rules we used to flag variances and the output you produced. Preview the skill, let me correct it, then run it on {xlsx2} and tell me if the result matches what we built here.",
        },
        'pp1': {
            'instr': "Open the finished deck in PowerPoint and open the **Copilot pane**. Type `@` to see the available skills, or pick one from the menu. Brand Kit and the prebuilt skills are generally available with a Microsoft 365 Copilot license (14 Sep 2026).",
            'prompt': "@Review Presentation Give me slide-by-slide, executive-level feedback on this deck for the {name} leadership team. Then use @Prepare for Questions to list the 10 hardest questions they are likely to ask and draft a short answer to each. Finally use @Visualize Slide on the slide with the most text and make it easier to read.",
        },
        'pp2': {
            'instr': "In the Copilot pane select **Create custom skill** (web from 23 Sep, Windows from 6 Oct 2026). Describe the skill in plain language, then test it on one slide before you rely on it.",
            'prompt': "Create a custom skill named {skill}-exec-slide. Whenever I ask for an executive summary slide for {name}, it should use one headline sentence, three supporting bullets with numbers taken from the source, a RAG status and one decision required. Then run the skill on slide 2 of this deck.",
        },
    },
    'BM': {
        'xl1': {
            'instr': "Buka buku kerja dalam Excel untuk web dan buka **anak tetingkap Copilot**. Dalam kotak gesaan pilih **Add** > **Choose plugins and skills**, atau taip `@` dan pilih satu skill. `@clean-data` sedang dilancarkan secara berperingkat, jadi ia mungkin belum tersedia pada semua tenant.",
            'prompt': "@clean-data Periksa {xlsx} untuk isu yang boleh merosakkan formula, carian, PivotTable dan laporan: ruang tambahan, format teks dan nombor yang tidak konsisten, tarikh yang tidak konsisten, nilai pendua dan nilai yang disimpan dengan jenis data yang salah. Terangkan apa yang anda jumpa dan mengapa ia penting untuk {name}, kemudian cadangkan pembetulan dan biar saya memilih perubahan mana yang hendak digunakan.",
        },
        'xl2': {
            'instr': "Kekal dalam anak tetingkap Copilot yang sama. Taip `@skill-builder` dan terangkan skill itu. Copilot memaparkan pratonton yang boleh anda baiki sebelum ia menyimpan skill ke folder skills dalam OneDrive anda. `@skill-builder` sedang dilancarkan secara berperingkat, jadi ia mungkin belum tersedia pada semua tenant.",
            'prompt': "@skill-builder Cipta skill bernama {skill}-monthly-review untuk pasukan {name}. Apabila saya meminta kajian bulanan, ia perlu membuka {xlsx}, memformat jadual utama, menyerlahkan varians negatif dengan warna merah, menambah carta ringkasan dan menulis ulasan tiga baris yang berakhir dengan satu tindakan yang disyorkan. {ctx}Tunjukkan pratonton kepada saya sebelum anda menyimpannya.",
        },
        'xl3': {
            'instr': "Lakukan ini selepas anda selesai satu tugas berbilang langkah bersama Copilot dalam sembang yang sama, contohnya prompt sebelumnya. Copilot menangkap langkah, peraturan keputusan dan output yang dijangka, dan memaparkan pratonton sebelum menyimpan.",
            'prompt': "Simpan apa yang baru kita lakukan sebagai skill baharu bernama {skill}-quarterly-pack. Tangkap langkah, peraturan yang kita guna untuk menandakan varians dan output yang anda hasilkan. Paparkan pratonton skill itu, biar saya membetulkannya, kemudian jalankannya pada {xlsx2} dan beritahu saya sama ada hasilnya sepadan dengan apa yang kita bina di sini.",
        },
        'pp1': {
            'instr': "Buka dek yang telah siap dalam PowerPoint dan buka **anak tetingkap Copilot**. Taip `@` untuk melihat skill yang ada, atau pilih satu daripada menu. Brand Kit dan skill sedia ada tersedia umum dengan lesen Microsoft 365 Copilot (14 Sep 2026).",
            'prompt': "@Review Presentation Berikan maklum balas peringkat eksekutif bagi setiap slaid untuk dek ini kepada pasukan kepimpinan {name}. Kemudian gunakan @Prepare for Questions untuk menyenaraikan 10 soalan paling sukar yang mungkin mereka tanya dan draf jawapan ringkas bagi setiap satu. Akhir sekali gunakan @Visualize Slide pada slaid yang paling banyak teks dan jadikannya lebih mudah dibaca.",
        },
        'pp2': {
            'instr': "Dalam anak tetingkap Copilot pilih **Create custom skill** (web mulai 23 Sep, Windows mulai 6 Okt 2026). Terangkan skill itu dalam bahasa biasa, kemudian uji pada satu slaid sebelum anda bergantung padanya.",
            'prompt': "Cipta skill tersuai bernama {skill}-exec-slide. Setiap kali saya meminta slaid ringkasan eksekutif untuk {name}, ia perlu menggunakan satu ayat tajuk, tiga poin sokongan dengan angka yang diambil daripada sumber, status RAG dan satu keputusan yang diperlukan. Kemudian jalankan skill itu pada slaid 2 dek ini.",
        },
    },
    'ID': {
        'xl1': {
            'instr': "Buka workbook di Excel untuk web dan buka **panel Copilot**. Di kotak prompt pilih **Add** > **Choose plugins and skills**, atau ketik `@` lalu pilih sebuah skill. `@clean-data` sedang diluncurkan bertahap, jadi mungkin belum tersedia di semua tenant.",
            'prompt': "@clean-data Periksa {xlsx} untuk masalah yang dapat merusak formula, lookup, PivotTable, dan laporan: spasi berlebih, format teks dan angka yang tidak konsisten, tanggal yang tidak konsisten, nilai duplikat, dan nilai yang tersimpan dengan tipe data yang salah. Jelaskan apa yang Anda temukan dan mengapa hal itu penting bagi {name}, lalu usulkan perbaikan dan biarkan saya memilih perubahan mana yang diterapkan.",
        },
        'xl2': {
            'instr': "Tetap di panel Copilot yang sama. Ketik `@skill-builder` dan jelaskan skill itu. Copilot menampilkan pratinjau yang dapat Anda sempurnakan sebelum menyimpan skill ke folder skills di OneDrive Anda. `@skill-builder` sedang diluncurkan bertahap, jadi mungkin belum tersedia di semua tenant.",
            'prompt': "@skill-builder Buat skill bernama {skill}-monthly-review untuk tim {name}. Saat saya meminta tinjauan bulanan, skill itu harus membuka {xlsx}, memformat tabel utama, menyorot varians negatif dengan warna merah, menambahkan grafik ringkasan, dan menulis komentar tiga baris yang diakhiri satu tindakan yang direkomendasikan. {ctx}Tampilkan pratinjau kepada saya sebelum Anda menyimpannya.",
        },
        'xl3': {
            'instr': "Lakukan ini setelah Anda menyelesaikan tugas multi-langkah bersama Copilot di chat yang sama, misalnya prompt sebelumnya. Copilot menangkap langkah, aturan keputusan, dan output yang diharapkan, lalu menampilkan pratinjau sebelum menyimpan.",
            'prompt': "Simpan apa yang baru saja kita kerjakan sebagai skill baru bernama {skill}-quarterly-pack. Tangkap langkah-langkahnya, aturan yang kita pakai untuk menandai varians, dan output yang Anda hasilkan. Tampilkan pratinjau skill itu, biarkan saya mengoreksinya, lalu jalankan pada {xlsx2} dan beri tahu saya apakah hasilnya sama dengan yang kita bangun di sini.",
        },
        'pp1': {
            'instr': "Buka deck yang sudah jadi di PowerPoint dan buka **panel Copilot**. Ketik `@` untuk melihat skill yang tersedia, atau pilih satu dari menu. Brand Kit dan skill bawaan tersedia umum dengan lisensi Microsoft 365 Copilot (14 September 2026).",
            'prompt': "@Review Presentation Berikan masukan tingkat eksekutif per slide untuk deck ini bagi tim pimpinan {name}. Lalu gunakan @Prepare for Questions untuk mendaftar 10 pertanyaan tersulit yang mungkin mereka ajukan dan menyusun jawaban singkat untuk masing-masing. Terakhir gunakan @Visualize Slide pada slide dengan teks paling banyak dan buat lebih mudah dibaca.",
        },
        'pp2': {
            'instr': "Di panel Copilot pilih **Create custom skill** (web mulai 23 September, Windows mulai 6 Oktober 2026). Jelaskan skill itu dengan bahasa sehari-hari, lalu uji pada satu slide sebelum Anda mengandalkannya.",
            'prompt': "Buat skill kustom bernama {skill}-exec-slide. Setiap kali saya meminta slide ringkasan eksekutif untuk {name}, skill itu harus memakai satu kalimat judul, tiga poin pendukung dengan angka yang diambil dari sumber, status RAG, dan satu keputusan yang diperlukan. Lalu jalankan skill itu pada slide 2 deck ini.",
        },
    },
}

_CTX_LABEL = {'EN': 'Context: ', 'BM': 'Konteks: ', 'ID': 'Konteks: '}
_ARRAYS = (('prompts', 'EN'), ('promptsBM', 'BM'), ('promptsID', 'ID'))
_GROUPS = (('xl1', 'xl2', 'xl3'), ('pp1', 'pp2'))


def _kind(label):
    label = str(label or '')
    if 'Copilot in Excel' in label:
        return 0
    if 'Copilot in PowerPoint' in label:
        return 1
    return None


def _clean_name(name):
    return re.sub(r'^[^A-Za-z0-9]+', '', str(name or '')).strip() or 'this team'


def _skill_base(entry):
    base = re.sub(r'^dept-', '', str(entry.get('id') or 'team').lower())
    base = re.sub(r'[^a-z0-9]+', '-', base).strip('-') or 'team'
    return base[:32].strip('-')


def _files(entry):
    xl = [str(f).lstrip('/') for f in (entry.get('files') or [])
          if str(f).lower().endswith('.xlsx') and not _SKIP_XLSX.match(str(f).lstrip('/'))]
    first = xl[0] if xl else 'the main workbook'
    second = xl[1] if len(xl) > 1 else first
    return first, second


def _ctx(entry, lang):
    key = {'EN': 'tagline', 'BM': 'taglineBM', 'ID': 'taglineID'}[lang]
    text = str(entry.get(key) or entry.get('tagline') or '').strip().replace('%%', '%')
    if not text:
        return ''
    if text[-1] not in '.!?':
        text += '.'
    return _CTX_LABEL[lang] + text + ' '


def _already_added(block):
    return any('@skill-builder' in str(p.get('prompt', '')) or 'Create a custom skill named' in str(p.get('prompt', ''))
               for p in (block.get('prompts') or []) if isinstance(p, dict))


def append_skills_prompts(entries):
    """Returns the number of English prompts appended across the entries."""
    added = 0
    for e in entries:
        name = _clean_name(e.get('name'))
        skill = _skill_base(e)
        xlsx, xlsx2 = _files(e)
        for block in e.get('prompts') or []:
            kind = _kind(block.get('tool'))
            if kind is None or _already_added(block):
                continue
            keys = _GROUPS[kind]
            aligned = {
                k: isinstance(block.get(k), list) and len(block.get(k)) == len(block.get('prompts') or [])
                for k in ('persona', 'personaID', 'personaBM')
            }
            for arr_key, lang in _ARRAYS:
                arr = block.get(arr_key)
                if not isinstance(arr, list):
                    continue
                fill = dict(name=name, skill=skill, xlsx=xlsx, xlsx2=xlsx2, ctx=_ctx(e, lang))
                new = [{'instr': T[lang][k]['instr'], 'prompt': T[lang][k]['prompt'].format(**fill)} for k in keys]
                block[arr_key] = list(arr) + new
            for pk in ('persona', 'personaID', 'personaBM'):
                seq = block.get(pk)
                if aligned[pk] and seq:
                    block[pk] = list(seq) + [seq[0]] * len(keys)
            added += len(keys)
    return added

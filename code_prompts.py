# -*- coding: utf-8 -*-
"""Copilot Code prompts (27 Oct 2026).

Adds a "Copilot Code (Frontier)" tool block with four prompts, in English, Bahasa
Malaysia and Bahasa Indonesia, to every industry and department entry. Each prompt is
filled from the entry's own name, sample workbooks and tagline, so the demo runs on
files the entry already ships. The block sits in the Microsoft 365 Copilot Tools tab,
right after Copilot in Teams.

Sources (Microsoft Learn, checked 27 Oct 2026):
  Overview        https://learn.microsoft.com/en-us/copilot/code/
  Get started     https://learn.microsoft.com/en-us/copilot/code/get-started
  Use Code        https://learn.microsoft.com/en-us/copilot/code/use-code
  Requirements    https://learn.microsoft.com/en-us/copilot/code/code-requirements
  Announcement    https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/
"""
import re

from util import DESC_CODE, FRONTIER_LIC, M365_ACCT, T_CODE, tool

_SKIP_XLSX = re.compile(r'^(Scout_|Autopilot_|Heartbeat_|00_Copilot)', re.I)

# One entry per prompt: instr (how to start) and prompt (what to paste).
T = {
    'EN': [
        {
            'instr': "Open the Microsoft Copilot app (or copilot.cloud.microsoft) and select **Code** in the tab switcher at the top. Choose **Cloud** so you can share the result and leave the model on **Auto**. Select **+** and upload {xlsx}, then paste the prompt below. Answer any clarifying questions and watch the live preview on the canvas.",
            'prompt': "Build an interactive dashboard from the attached workbook for the {name} leadership team. Show the six most important KPIs as tiles with a small trend line, a filter bar for the three most useful dimensions, a ranked table with drill-down and red, amber and green flags against target. Keep it to one screen and tell me every assumption you make. {ctx}",
        },
        {
            'instr': "Stay in the same Code project. Check the preview and ask for one change at a time. Building does not publish the app, so publishing is a separate step: when you are happy, ask Code to publish it, then ask Code to share it with specific people or groups in your organization. Apps run on Copilot Managed Runtime (preview). People you share with see only the data they already have permission to open.",
            'prompt': "Build an app that tracks the open actions from the weekly {name} review. Each action has a title, owner, due date, status (Not started, In progress, Blocked, Done) and a RAG flag. Add a form to create actions, a kanban view by status, a counter of overdue actions and a button that exports the open actions to CSV. Use sample rows from {xlsx2} so the preview looks real. Show me the preview first and do not publish until I say so.",
        },
        {
            'instr': "Start a new Code project in **Cloud** mode and attach {xlsx}. Paste the prompt, review the preview and refine one change at a time. When you are happy, ask Code to share the static app as a link. The link is scoped to your organization, so only people in your organization can open it.",
            'prompt': "Create a one-page static website that summarises this week's {name} briefing for managers. Include a headline, three key numbers from the attached workbook with a plain-language explanation of each, a short list of risks and decisions, and a sources section that names the files used. Make it mobile-friendly and easy to print. {ctx}",
        },
        {
            'instr': "Start a new Code project in **Local** mode and open a folder that holds {xlsx} and {xlsx2}. Pick a model, because **Auto** is cloud only. Code asks for your approval before it reaches outside the folder, makes a network call, uses extensions or MCP, or runs a shell command, so read each consent prompt before you allow it.",
            'prompt': "Write a script that reads {xlsx} and {xlsx2}, joins them on the shared identifier column, flags rows that fail basic checks (missing values, duplicates, values outside the expected range) and writes exceptions.csv plus a one-paragraph summary of what you found for {name}. Explain each step in plain language before you run it, and tell me which files you read and wrote.",
        },
    ],
    'BM': [
        {
            'instr': "Buka aplikasi Microsoft Copilot (atau copilot.cloud.microsoft) dan pilih **Code** pada pensuis tab di bahagian atas. Pilih **Cloud** supaya anda boleh berkongsi hasilnya dan biarkan model pada **Auto**. Pilih **+** dan muat naik {xlsx}, kemudian tampal prompt di bawah. Jawab sebarang soalan penjelasan dan perhatikan pratonton langsung pada kanvas.",
            'prompt': "Bina papan pemuka interaktif daripada buku kerja yang dilampirkan untuk pasukan kepimpinan {name}. Paparkan enam KPI terpenting sebagai jubin dengan garis aliran kecil, bar penapis untuk tiga dimensi yang paling berguna, jadual berperingkat dengan drill-down dan bendera merah, kuning dan hijau berbanding sasaran. Pastikan ia muat pada satu skrin dan beritahu saya setiap andaian yang anda buat. {ctx}",
        },
        {
            'instr': "Kekal dalam projek Code yang sama. Semak pratonton dan minta satu perubahan pada satu masa. Membina tidak menerbitkan aplikasi, jadi penerbitan ialah langkah berasingan: apabila anda berpuas hati, minta Code menerbitkannya, kemudian minta Code berkongsinya dengan orang atau kumpulan tertentu dalam organisasi anda. Aplikasi berjalan pada Copilot Managed Runtime (pratonton). Orang yang anda kongsikan hanya melihat data yang sudah mereka ada kebenaran untuk dibuka.",
            'prompt': "Bina aplikasi untuk menjejaki tindakan terbuka daripada kajian mingguan {name}. Setiap tindakan mempunyai tajuk, pemilik, tarikh akhir, status (Belum bermula, Sedang dijalankan, Tersekat, Selesai) dan bendera RAG. Tambah borang untuk mencipta tindakan, paparan kanban mengikut status, pembilang tindakan yang tertunggak dan butang yang mengeksport tindakan terbuka ke CSV. Gunakan baris contoh daripada {xlsx2} supaya pratonton kelihatan nyata. Tunjukkan pratonton dahulu dan jangan terbitkan sehingga saya beritahu.",
        },
        {
            'instr': "Mulakan projek Code baharu dalam mod **Cloud** dan lampirkan {xlsx}. Tampal prompt, semak pratonton dan perhalusi satu perubahan pada satu masa. Apabila anda berpuas hati, minta Code berkongsi aplikasi statik itu sebagai pautan. Pautan itu terhad kepada organisasi anda, jadi hanya orang dalam organisasi anda boleh membukanya.",
            'prompt': "Cipta laman web statik satu halaman yang merumuskan taklimat {name} minggu ini untuk pengurus. Sertakan tajuk utama, tiga angka utama daripada buku kerja yang dilampirkan dengan penjelasan ringkas bagi setiap satu, senarai pendek risiko dan keputusan, serta bahagian sumber yang menamakan fail yang digunakan. Jadikan ia mesra telefon bimbit dan mudah dicetak. {ctx}",
        },
        {
            'instr': "Mulakan projek Code baharu dalam mod **Local** dan buka folder yang mengandungi {xlsx} dan {xlsx2}. Pilih model, kerana **Auto** hanya untuk cloud. Code meminta kelulusan anda sebelum ia keluar dari folder, membuat panggilan rangkaian, menggunakan sambungan atau MCP, atau menjalankan arahan shell, jadi baca setiap gesaan persetujuan sebelum anda membenarkannya.",
            'prompt': "Tulis skrip yang membaca {xlsx} dan {xlsx2}, menggabungkannya pada lajur pengecam yang dikongsi, menandakan baris yang gagal semakan asas (nilai hilang, pendua, nilai di luar julat yang dijangka) dan menulis exceptions.csv serta satu perenggan rumusan tentang apa yang anda jumpa untuk {name}. Terangkan setiap langkah dalam bahasa biasa sebelum anda menjalankannya, dan beritahu saya fail mana yang anda baca dan tulis.",
        },
    ],
    'ID': [
        {
            'instr': "Buka aplikasi Microsoft Copilot (atau copilot.cloud.microsoft) dan pilih **Code** pada pengalih tab di bagian atas. Pilih **Cloud** agar Anda dapat membagikan hasilnya dan biarkan model pada **Auto**. Pilih **+** dan unggah {xlsx}, lalu tempel prompt di bawah. Jawab pertanyaan klarifikasi jika ada dan lihat pratinjau langsung di kanvas.",
            'prompt': "Buat dashboard interaktif dari workbook terlampir untuk tim pimpinan {name}. Tampilkan enam KPI terpenting sebagai tile dengan garis tren kecil, bilah filter untuk tiga dimensi yang paling berguna, tabel berperingkat dengan drill-down, dan bendera merah, kuning, dan hijau terhadap target. Jaga agar muat dalam satu layar dan beri tahu saya setiap asumsi yang Anda buat. {ctx}",
        },
        {
            'instr': "Tetap di proyek Code yang sama. Periksa pratinjau dan minta satu perubahan dalam satu waktu. Membangun tidak menerbitkan aplikasi, jadi penerbitan adalah langkah terpisah: saat Anda sudah puas, minta Code menerbitkannya, lalu minta Code membagikannya kepada orang atau grup tertentu di organisasi Anda. Aplikasi berjalan di Copilot Managed Runtime (pratinjau). Orang yang menerima hanya melihat data yang sudah boleh mereka buka.",
            'prompt': "Buat aplikasi untuk melacak tindakan yang masih terbuka dari tinjauan mingguan {name}. Setiap tindakan memiliki judul, pemilik, tenggat, status (Belum mulai, Sedang berjalan, Terhambat, Selesai), dan bendera RAG. Tambahkan formulir untuk membuat tindakan, tampilan kanban menurut status, penghitung tindakan yang terlambat, dan tombol yang mengekspor tindakan terbuka ke CSV. Gunakan baris contoh dari {xlsx2} agar pratinjau terlihat nyata. Tampilkan pratinjau dulu dan jangan terbitkan sampai saya katakan.",
        },
        {
            'instr': "Mulai proyek Code baru dalam mode **Cloud** dan lampirkan {xlsx}. Tempel prompt, periksa pratinjau, dan sempurnakan satu perubahan dalam satu waktu. Saat Anda sudah puas, minta Code membagikan aplikasi statis itu sebagai tautan. Tautan itu terbatas pada organisasi Anda, jadi hanya orang di organisasi Anda yang dapat membukanya.",
            'prompt': "Buat situs web statis satu halaman yang merangkum briefing {name} minggu ini untuk para manajer. Sertakan judul utama, tiga angka kunci dari workbook terlampir dengan penjelasan singkat untuk masing-masing, daftar singkat risiko dan keputusan, serta bagian sumber yang menyebut file yang dipakai. Buat ramah ponsel dan mudah dicetak. {ctx}",
        },
        {
            'instr': "Mulai proyek Code baru dalam mode **Local** dan buka folder yang berisi {xlsx} dan {xlsx2}. Pilih model, karena **Auto** hanya untuk cloud. Code meminta persetujuan Anda sebelum keluar dari folder, melakukan panggilan jaringan, memakai ekstensi atau MCP, atau menjalankan perintah shell, jadi baca setiap permintaan persetujuan sebelum Anda mengizinkannya.",
            'prompt': "Tulis skrip yang membaca {xlsx} dan {xlsx2}, menggabungkannya pada kolom pengenal yang sama, menandai baris yang gagal pemeriksaan dasar (nilai kosong, duplikat, nilai di luar rentang yang diharapkan), dan menulis exceptions.csv beserta satu paragraf ringkasan temuan untuk {name}. Jelaskan setiap langkah dengan bahasa sederhana sebelum Anda menjalankannya, dan beri tahu saya file mana yang Anda baca dan tulis.",
        },
    ],
}

_CTX_LABEL = {'EN': 'Context: ', 'BM': 'Konteks: ', 'ID': 'Konteks: '}


def _clean_name(name):
    return re.sub(r'^[^A-Za-z0-9]+', '', str(name or '')).strip() or 'this team'


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
    return _CTX_LABEL[lang] + text


def _persona(entry):
    personas = entry.get('personas') or []
    if personas and isinstance(personas[0], dict):
        return personas[0].get('name') or 'Hadar Caspit'
    return 'Hadar Caspit'


def _fill(lang, entry):
    xlsx, xlsx2 = _files(entry)
    values = dict(name=_clean_name(entry.get('name')), xlsx=xlsx, xlsx2=xlsx2, ctx=_ctx(entry, lang))
    return [{'instr': p['instr'].format(**values).strip(), 'prompt': p['prompt'].format(**values).strip()}
            for p in T[lang]]


def append_code_blocks(entries):
    """Adds the Copilot Code block to each entry. Returns the number of entries changed."""
    added = 0
    for e in entries:
        blocks = e.get('prompts')
        if not isinstance(blocks, list) or any(isinstance(b, dict) and b.get('tool') == T_CODE for b in blocks):
            continue
        en, bm, idn = _fill('EN', e), _fill('BM', e), _fill('ID', e)
        persona = _persona(e)
        block = tool(
            T_CODE, FRONTIER_LIC, M365_ACCT, en,
            desc=DESC_CODE,
            promptsID=idn,
            promptsBM=bm,
            persona=[persona] * len(en),
            personaID=[persona] * len(en),
        )
        at = len(blocks)
        for i, b in enumerate(blocks):
            if isinstance(b, dict) and 'Teams' in str(b.get('tool') or ''):
                at = i + 1
                break
        e['prompts'] = blocks[:at] + [block] + blocks[at:]
        added += 1
    return added

# Если застрял: маршрут первичной проверки

Маршруты ниже используют только реально присутствующие в проекте шпаргалки и скрипты. Запускай команды на локальных учебных файлах или в разрешённой среде.

## Я вижу ELF

**Порядок:** file → strings → checksec → readelf → objdump → GDB → Ghidra.

**Шпаргалки:** [07 REVERSE](../07_CHEATSHEETS/07_REVERSE.md), [05 GDB](../07_CHEATSHEETS/05_GDB.md), [06 GHIDRA](../07_CHEATSHEETS/06_GHIDRA.md)

**Локальные scripts:** [elf_triage.py](../scripts/elf_triage.py), [01_elf.sh](../scripts/reverse/01_elf.sh), [04_disasm.sh](../scripts/reverse/04_disasm.sh), [08_gdb_main.sh](../scripts/reverse/08_gdb_main.sh)

**Следующий шаг:** открой соответствующие темы в [TRAIN_MANUAL](../docs/TRAIN_MANUAL.md) и выполни практику из них. Не запускай неизвестный бинарник; сверяй ограничения и доступность команды в [TOOL_INDEX](../docs/TOOL_INDEX.md).

## Я вижу PCAP

**Порядок:** tshark → Wireshark → протоколы/фильтры → DNS и TCP streams.

**Шпаргалки:** [20 NETWORK](../07_CHEATSHEETS/20_NETWORK.md), [21 TSHARK](../07_CHEATSHEETS/21_TSHARK.md), [22 WIRESHARK](../07_CHEATSHEETS/22_WIRESHARK.md)

**Локальные scripts:** [pcap_summary.py](../scripts/pcap_summary.py), [02_pcap_protocols.sh](../scripts/network/02_pcap_protocols.sh), [03_dns.sh](../scripts/network/03_dns.sh), [05_tcp_streams.sh](../scripts/network/05_tcp_streams.sh), [07_tcp_follow.sh](../scripts/network/07_tcp_follow.sh)

**Следующий шаг:** открой соответствующие темы в [TRAIN_MANUAL](../docs/TRAIN_MANUAL.md) и выполни практику из них. Не запускай неизвестный бинарник; сверяй ограничения и доступность команды в [TOOL_INDEX](../docs/TOOL_INDEX.md).

## Я вижу PNG или изображение

**Порядок:** file → exiftool → strings → binwalk → zsteg → проверка PNG chunks/LSB.

**Шпаргалки:** [18 FORENSICS](../07_CHEATSHEETS/18_FORENSICS.md), [19 STEGO](../07_CHEATSHEETS/19_STEGO.md), [33 FILE FORMATS](../07_CHEATSHEETS/33_FILE_FORMATS.md)

**Локальные scripts:** [06_metadata.sh](../scripts/forensics/06_metadata.sh), [07_signatures.sh](../scripts/forensics/07_signatures.sh), [png_chunks.py](../scripts/png_chunks.py), [lsb_image.py](../scripts/lsb_image.py), [bruteforce_lowbits.py](../scripts/bruteforce_lowbits.py)

**Следующий шаг:** открой соответствующие темы в [TRAIN_MANUAL](../docs/TRAIN_MANUAL.md) и выполни практику из них. Не запускай неизвестный бинарник; сверяй ограничения и доступность команды в [TOOL_INDEX](../docs/TOOL_INDEX.md).

## Я вижу неизвестный файл/архив

**Порядок:** file → xxd → strings → hash → archive listing, затем первичная сортировка.

**Шпаргалки:** [18 FORENSICS](../07_CHEATSHEETS/18_FORENSICS.md), [33 FILE FORMATS](../07_CHEATSHEETS/33_FILE_FORMATS.md), [36 USEFUL ONE LINERS](../07_CHEATSHEETS/36_USEFUL_ONE_LINERS.md)

**Локальные scripts:** [file_triage.py](../scripts/file_triage.py), [magic_scan.py](../scripts/magic_scan.py), [10_triage.sh](../scripts/forensics/10_triage.sh)

**Следующий шаг:** открой соответствующие темы в [TRAIN_MANUAL](../docs/TRAIN_MANUAL.md) и выполни практику из них. Не запускай неизвестный бинарник; сверяй ограничения и доступность команды в [TOOL_INDEX](../docs/TOOL_INDEX.md).

## Я вижу веб-адрес или HTTP задачу

**Порядок:** curl headers/body → robots/sitemap → разрешённое перечисление → формы/JSON.

**Шпаргалки:** [10 WEB](../07_CHEATSHEETS/10_WEB.md), [24 ENUMERATION](../07_CHEATSHEETS/24_ENUMERATION.md), [27 GOBUSTER](../07_CHEATSHEETS/27_GOBUSTER.md)

**Локальные scripts:** [web_probe.py](../scripts/web_probe.py), [01_headers.sh](../scripts/web/01_headers.sh), [03_robots.sh](../scripts/web/03_robots.sh), [04_sitemap.sh](../scripts/web/04_sitemap.sh), [08_forms.sh](../scripts/web/08_forms.sh)

**Следующий шаг:** открой соответствующие темы в [TRAIN_MANUAL](../docs/TRAIN_MANUAL.md) и выполни практику из них. Не запускай неизвестный бинарник; сверяй ограничения и доступность команды в [TOOL_INDEX](../docs/TOOL_INDEX.md).

## Я вижу XOR/Base64/RSA или хеш

**Порядок:** определи кодировку/примитив → проверь формат и параметры → применяй узкий helper.

**Шпаргалки:** [16 CRYPTO](../07_CHEATSHEETS/16_CRYPTO.md), [17 HASHES](../07_CHEATSHEETS/17_HASHES.md), [34 ENCODING](../07_CHEATSHEETS/34_ENCODING.md)

**Локальные scripts:** [base_decode.py](../scripts/base_decode.py), [xor_singlebyte.py](../scripts/xor_singlebyte.py), [rsa_helpers.py](../scripts/rsa_helpers.py), [lcg_solver.py](../scripts/lcg_solver.py), [hash_report.py](../scripts/hash_report.py)

**Следующий шаг:** открой соответствующие темы в [TRAIN_MANUAL](../docs/TRAIN_MANUAL.md) и выполни практику из них. Не запускай неизвестный бинарник; сверяй ограничения и доступность команды в [TOOL_INDEX](../docs/TOOL_INDEX.md).

## Я вижу Windows PE или дамп памяти

**Порядок:** определи формат → PE triage или Volatility 3; проверь tool index и наличие профиля/символов.

**Шпаргалки:** [28 WINDOWS](../07_CHEATSHEETS/28_WINDOWS.md), [30 VOLATILITY](../07_CHEATSHEETS/30_VOLATILITY.md), [32 MALWARE ANALYSIS](../07_CHEATSHEETS/32_MALWARE_ANALYSIS.md)

**Локальные scripts:** [pe_triage.py](../scripts/pe_triage.py), [vol.py](../scripts/vol.py), [10_triage.sh](../scripts/forensics/10_triage.sh)

**Следующий шаг:** открой соответствующие темы в [TRAIN_MANUAL](../docs/TRAIN_MANUAL.md) и выполни практику из них. Не запускай неизвестный бинарник; сверяй ограничения и доступность команды в [TOOL_INDEX](../docs/TOOL_INDEX.md).

## Я вижу Pwn бинарник

**Порядок:** checksec → символы/строки → offset → локальный debugger → шаблон только в локальной задаче.

**Шпаргалки:** [08 PWN](../07_CHEATSHEETS/08_PWN.md), [09 PWNLIB](../07_CHEATSHEETS/09_PWNLIB.md), [05 GDB](../07_CHEATSHEETS/05_GDB.md)

**Локальные scripts:** [01_checksec.sh](../scripts/pwn/01_checksec.sh), [02_pattern.sh](../scripts/pwn/02_pattern.sh), [03_offset.sh](../scripts/pwn/03_offset.sh), [10_local_check.sh](../scripts/pwn/10_local_check.sh), [offset_finder.py](../scripts/offset_finder.py), [rop_template.py](../scripts/rop_template.py)

**Следующий шаг:** открой соответствующие темы в [TRAIN_MANUAL](../docs/TRAIN_MANUAL.md) и выполни практику из них. Не запускай неизвестный бинарник; сверяй ограничения и доступность команды в [TOOL_INDEX](../docs/TOOL_INDEX.md).

Для общей методики: [65. Дерево первичной сортировки](../docs/TRAIN_MANUAL.md#65-дерево-первичной-сортировки), [66. Что делать, если застрял](../docs/TRAIN_MANUAL.md#66-что-делать-если-застрял), [67. Проверка перед отправкой флага](../docs/TRAIN_MANUAL.md#67-проверка-перед-отправкой-флага).

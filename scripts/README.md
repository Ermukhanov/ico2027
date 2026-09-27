# Вспомогательные shell-сценарии

60 тематических сценариев ниже дополняют Python-инструменты из каталога `scripts/`. Перед запуском открой исходник, проверь аргументы и используй только локальные файлы или адреса, разрешённые правилами соревнования. Сценарии в `network/` и `web/` могут обращаться к сети.

## Форензика

- `forensics/01_file_type.sh` — определить тип файла.
- `forensics/02_hash.sh` — вычислить хеш файла.
- `forensics/03_strings.sh` — извлечь читаемые строки.
- `forensics/04_hex_header.sh` — посмотреть первые 256 байт.
- `forensics/05_hex_tail.sh` — посмотреть последние 256 байт.
- `forensics/06_metadata.sh` — проверить метаданные.
- `forensics/07_signatures.sh` — найти встроенные сигнатуры.
- `forensics/08_carve.sh` — извлечь файлы по узнаваемым сигнатурам.
- `forensics/09_entropy.sh` — оценить энтропию.
- `forensics/10_triage.sh` — выполнить полный сценарий первичной проверки.

## Криптография

- `crypto/01_hashes.sh` — вывести распространённые хеши.
- `crypto/02_base.sh` — проверить распространённые Base-кодировки.
- `crypto/03_xor.sh` — ранжировать однобайтовые XOR-ключи.
- `crypto/04_lcg_solve.sh` — восстановить параметры LCG по трём состояниям.
- `crypto/05_lcg_predict.sh` — предсказать следующие состояния LCG.
- `crypto/06_mod_inverse.sh` — вычислить обратный элемент по модулю.
- `crypto/07_factor.sh` — разложить небольшое целое число на множители.
- `crypto/08_z3_demo.sh` — запустить небольшой пример ограничений Z3.
- `crypto/09_padding.sh` — вычислить размер SHA-подобного дополнения.
- `crypto/10_length_extension_notes.sh` — вывести заметки об удлинении хеша.

## Сеть

- `network/01_pcap_info.sh` — сводка по захвату трафика.
- `network/02_pcap_protocols.sh` — иерархия протоколов.
- `network/03_dns.sh` — извлечь DNS-запросы.
- `network/04_dns_unique.sh` — перечислить уникальные DNS-запросы.
- `network/05_tcp_streams.sh` — перечислить TCP-потоки.
- `network/06_http.sh` — показать HTTP-запросы.
- `network/07_tcp_follow.sh` — проследить TCP-поток 0.
- `network/08_tls.sh` — исследовать рукопожатия TLS.
- `network/09_flows.sh` — свести сетевые потоки IP.
- `network/10_dns_decode.sh` — соединить DNS-метки и проверить декодирование.

## Reverse engineering

- `reverse/01_elf.sh` — сводка по ELF.
- `reverse/02_sections.sh` — перечислить секции ELF.
- `reverse/03_symbols.sh` — перечислить символы.
- `reverse/04_disasm.sh` — дизассемблировать в синтаксисе Intel.
- `reverse/05_strings.sh` — найти интересные строки в бинарнике.
- `reverse/06_libs.sh` — показать динамические зависимости.
- `reverse/07_checksec.sh` — показать защиты от эксплуатации.
- `reverse/08_gdb_main.sh` — неинтерактивно дизассемблировать `main`.
- `reverse/09_pe.sh` — сводка по PE.
- `reverse/10_magic.sh` — искать встроенные сигнатуры.

## Pwn

- `pwn/01_checksec.sh` — проверить защиты бинарника.
- `pwn/02_pattern.sh` — сгенерировать циклический шаблон.
- `pwn/03_offset.sh` — найти смещение в циклическом шаблоне.
- `pwn/04_gadgets.sh` — перечислить ROP-gadget.
- `pwn/05_pop_rdi.sh` — найти последовательность `pop rdi`.
- `pwn/06_symbols.sh` — найти вероятные символы `win`/`flag`/`admin`.
- `pwn/07_strings.sh` — найти целевые строки.
- `pwn/08_rop_template.sh` — вывести шаблон для ROP.
- `pwn/09_fmt_template.sh` — вывести шаблон для format-string задачи.
- `pwn/10_local_check.sh` — выполнить безопасную локальную проверку.

## Web

- `web/01_headers.sh` — получить HTTP-заголовки.
- `web/02_page.sh` — сохранить главную страницу.
- `web/03_robots.sh` — проверить `robots.txt`.
- `web/04_sitemap.sh` — проверить `sitemap.xml`.
- `web/05_wp.sh` — проверить WordPress REST API.
- `web/06_options.sh` — проверить HTTP-методы.
- `web/07_probe.sh` — проверить распространённые CTF-пути.
- `web/08_forms.sh` — разобрать сохранённые HTML-формы.
- `web/09_json.sh` — вывести пути ключей JSON.
- `web/10_sqli_baseline.sh` — отправить базовую SQLi-проверку только разрешённой цели.

## Volatility 3

- `vol.py` — запускает локальный checkout `05_REPOS/volatility3` через проектный Python и кэш `.cache/volatility3`.
- Быстрая проверка: `scripts/vol.py -h`.
- Без дампа выполни `scripts/vol.py frameworkinfo.FrameworkInfo`; для анализа передай `-f MEMORY` и подходящий плагин.

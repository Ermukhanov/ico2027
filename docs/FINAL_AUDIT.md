# Final ICO 2027 Preparation Audit

Проверено 27 сентября 2026 года в `/home/zuck/ico2027`. Это audit текущего checkout и среды Codex; наличие внешней цели/медиа не предполагается без локального файла.

## Completed

- Русскоязычный маршрут `START_HERE` → 1h → 6h → manual → шпаргалки/scripts → ICO writeup/tasks → mini-CTF.
- В `TRAIN_MANUAL.md` — 68 тем `00–67`; все обязательные практические секции проверены.
- `SCRIPT_INDEX.md` перечисляет все 96 Python/shell-файлов. В `scripts/` 37 файлов первого уровня.
- Созданы 39 тематических шпаргалок и навигация в `07_CHEATSHEETS/README.md`.
- Создан `06_MINI_CTF/`: 12 задач (2 Reverse, 2 Pwn, 2 Web, 2 Crypto, 2 Forensics, 1 Stego, 1 Networking) с локальными артефактами, условиями, решателями и writeup.
- В `08_BOOKS/README.md` перечислены бесплатные/легальные онлайн-материалы и уже имеющиеся локальные справочники; книги без подтверждённой лицензии не копировались.
- В `09_VIDEOS/README.md` и `VIDEO_INDEX.md` каталогизированы онлайн-кандидаты по языку/теме. Файлы видео не заявлены как загруженные.
- Добавлен `scripts/vol.py`: запускает Volatility из локального source checkout через `.venv` и project cache.
- `tools/README.md` объясняет, где находятся установленные программы; не создаёт дубликаты бинарников.

## Remaining limitations

- Challenge-бинарники и часть медиа ICO 2027 в checkout отсутствуют; qualifying writeup указывает на внешний Google Drive. Их локальная доступность/разрешение на скачивание не подтверждены.
- В `09_VIDEOS/` нет локальных видео. Большинство старых YouTube-ссылок не удалось повторно открыть средством проверки; они помечены как ONLINE ONLY, но актуальную доступность нужно проверить при наличии сети.
- В `08_BOOKS/` нет отдельных PDF/EPUB книг. Для поездки доступны локальные руководства и документация в репозиториях; полные онлайн-курсы требуют сети.
- Для анализа Volatility не найден memory dump. CLI и плагин `frameworkinfo.FrameworkInfo` работают, но результат форензики образа памяти не проверен.
- GUI-запуск Ghidra в этой headless-сессии не подтверждён. `docker`, `masscan`, `feroxbuster`, `ncat`, `ropper`, `gef`, `pwndbg` и команда `volatility3` в PATH отсутствуют. Альтернативы и статусы описаны в TOOL_INDEX.
- Среда блокировала создание loopback-сокета, поэтому интерактивный запуск mini-CTF web server не проверен здесь. Условие решается офлайн напрямую вызовом локального handler; приложение привязано к `127.0.0.1`.
- `07_CHEATSHEETS/`, `06_MINI_CTF/` и `tools/` — дополнения проекта, но основной каталог не является Git working tree. См. ниже статусы вложенных репозиториев.

## Offline capabilities

- Локально доступны документация, 39 шпаргалок, все mini-CTF артефакты, ICO 2025 checkout/архивы, ICO 2027 writeup/изображения, 75 wheel-файлов и 42 установочных файла.
- Python dependencies работают в `.venv`; `pip check` проходит. Локальные Gobuster/YARA/zsteg/Ghidra/jq требуют `source scripts/local_tools_env.sh`.
- Активные запросы к внешним сайтам/соревновательным целям, видео и внешние ICO 2027 challenge assets без сети недоступны.

## Installed tools

Проверены команды `file`, `strings`, `xxd`, `od`, grep/sed/awk/find/xargs, curl/wget/nc/nmap, ffuf, Gobuster, jq, Python, GDB, Pwntools, objdump/readelf/nm/ldd, strace/ltrace, checksec/patchelf/ROPgadget, Ghidra (команда доступна), radare2, tshark/Wireshark/Scapy, binwalk/foremost/exiftool/zsteg/steghide, John/Hashcat, OpenSSL, YARA, SQLite, Git и socat. Точный статус/минимальные команды смотри в `TOOL_INDEX.md`.

`hexdump` отсутствует — используй `xxd` или `od`. Для `masscan`/`feroxbuster` — `nmap`/`ffuf`/Gobuster; для `ncat` — `nc`/socat; для GEF/pwndbg — базовый GDB. `volatility3` как PATH-команда отсутствует, но project wrapper работает.

## Python environment

- `.venv/bin/python`: Python 3.14.7.
- `pip check`: успешно, ошибок зависимостей нет.
- Подтверждены imports pwntools, Scapy, PyCryptodome, z3, requests, pyelftools, pefile, capstone, Pillow и NumPy.
- Используй `.venv/bin/python` для решателей и библиотек проекта.

## Repositories

Существуют все семь checkout: `ico-tasks`, `pwntools`, `PayloadsAllTheThings`, `SecLists`, `hacktricks`, `ctf-wiki`, `volatility3`. Повторное клонирование не выполнялось. При финальной проверке SecLists имел 17 локально удалённых путей, HackTricks — три прежних удаления и одну изменённую README-ссылку. Эти состояния не сбрасывались. Остальные пять checkout чистые.

Основной nested repo `ico-2027` имеет изменённый `ico_qualifying_round/ico_ctf_writeup.md` из предыдущей работы; изменение сохранено, commit не выполнялся.

## Wordlists

Пять ссылок в `wordlists/` разрешаются в SecLists: `common.txt`, `raft-small-directories.txt`, `raft-small-words.txt`, `top-usernames-shortlist.txt`, `rockyou.txt.tar.gz`. Копий словарей не создавалось.

## Training materials

`START_HERE.md` ведёт через crash course, шестичасовой план, 68-темный manual, шпаргалки/скрипты, ICO материалы и mini-CTF. `5H_TRAINING_PLAN.md` занимает шесть часов по блокам; это указано в самом документе.

## Cheatsheets

39 отдельных страниц плюс README в `07_CHEATSHEETS/`: Linux, Bash, Python, Git, GDB/Ghidra, Reverse/Pwn/Pwntools, Web/SQLi/XSS/SSRF/LFI/command injection, Crypto/Hashes, Forensics/Stego/Network/PCAP, Nmap/fuzzing, Windows/PowerShell, Volatility/YARA/malware, форматы, encoding, regex, методика CTF и OSINT.

## Books

`08_BOOKS/README.md` содержит секции Recommended, Free / Legal, Already available locally, Online only, Why useful и Relevant ICO topics. Крупные CTF Wiki/HackTricks/PayloadsAllTheThings уже локальны; они не скопированы повторно. Отдельные легально распространяемые офлайн-книги не подтверждены.

## Videos

В индексе 9 YouTube-карточек, все `ONLINE ONLY`; локальных видеофайлов — 0. Русский приоритет и тематическая навигация присутствуют. Фактическую доступность части старых ссылок перепроверь перед поездкой.

## ICO 2025

Локальный `05_REPOS/ico-tasks/` содержит qualifying/finals материалы, описания и четыре ZIP-архива finals. Manual и crash course направляют к локальным задачам. Не каждый удалённый attachment входит в checkout.

## ICO 2027

В `ico-2027/` присутствуют rules, qualifying writeup и task illustrations. Сам writeup указывает, что challenge binaries/media находятся отдельно; они не заявлены как локально скачанные. Archived ICO материалы также сохранены.

## Scripts

96 Python/shell-файлов перечислены в `SCRIPT_INDEX.md`. В дополнение создан `scripts/vol.py`; все Python исходники компилируются, shell-синтаксис корректен. `scripts/local_tools_env.sh` намеренно используется через `source`, поэтому ему не требуется executable bit.

## Verification results

- `python3 -m compileall -q scripts` — успешно.
- `find scripts -type f -name '*.sh' -print0 | xargs -0 -n1 bash -n` — успешно.
- `.venv/bin/python -m pip check` — успешно.
- `bash scripts/offline_test.sh` — успешно: импорты и команды из списка теста доступны.
- Volatility `-h` и `frameworkinfo.FrameworkInfo` — успешно без внешней сети/дампа.
- Все 12 mini-CTF solve scripts — успешно; локальный web handler протестирован без сокета.
- Проверены 117 поддерживаемых Markdown-документов/README: 0 несуществующих внутренних ссылок.
- Все пять wordlist symlink-ов разрешаются; 39 cheat sheets содержат требуемые разделы.

## Backup

Полный базовый архив `99_BACKUP/ico2027-full-final.tar.gz` сохранён и проверен по имеющейся SHA-256 сумме. Существенные дополнения этого завершения упакованы в `99_BACKUP/ico2027-final-completion.tar.gz`; его SHA-256 хранится также в `99_BACKUP/SHA256SUMS-final-completion.txt`. Значение записано в этот текущий audit после упаковки; snapshot отчёта внутри архива указывает sidecar. Архив incremental, не копия 4 GB полного backup.

`ico2027-final-completion.tar.gz`: `ceb279eff9c1dccfaf37af74afeca9d1abf95e41312f7d1874352f71a3fbeabb`

## How to start training

    cd /home/zuck/ico2027 && source scripts/local_tools_env.sh && source .venv/bin/activate && cat docs/START_HERE.md

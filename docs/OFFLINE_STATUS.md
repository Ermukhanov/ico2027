# Состояние офлайн-подготовки

Состояние проверено 27 сентября 2026 года в текущем окружении. Поскольку системный PATH и окружение проекта различаются, команды `gobuster`, `yara`, `zsteg` и `ghidra` проверены после загрузки `scripts/local_tools_env.sh`.

## Python и зависимости

В каталоге `.venv` находятся требуемые Python-библиотеки, включая pwntools, Scapy, PyCryptodome, z3, requests, pyelftools, pefile и capstone. Вызов `scripts/offline_test.sh` подтвердил импорты. Системный Python отличается от проектного окружения: для задач используй `.venv`.

Локальная установка из wheelhouse:

```bash
cd /home/zuck/ico2027
source .venv/bin/activate
python -m pip install --no-index --find-links 10_WHEELS --only-binary=unicorn -r docs/requirements.txt
python -m pip check
```

Для `unicorn` используется совместимое двоичное колесо из локальной коллекции. Не устанавливай библиотеки в системный Python через `sudo pip`.

## Репозитории

Все перечисленные checkout уже есть; не клонируй их поверх существующих файлов. Хеши коммитов зафиксированы по локальному отчёту подготовки.

| Репозиторий | Адрес проекта | Коммит |
|---|---|---|
| `ico-tasks` | `https://github.com/bysmaks/ico-tasks.git` | `48b52b28e75e3b1dfebeb3820ef1ed6f4cdb654e` |
| `pwntools` | `https://github.com/Gallopsled/pwntools.git` | `1429a134ecf88eb9af70e05bf6c912f45dfde224` |
| `PayloadsAllTheThings` | `https://github.com/swisskyrepo/PayloadsAllTheThings.git` | `3ac27901c711bdf3f5b65a7b1d1820a1f65bd09a` |
| `SecLists` | `https://github.com/danielmiessler/SecLists.git` | `39166b57cfcc73afd87081cfb20bd317cdece6ff` |
| `hacktricks` | `https://github.com/HackTricks-wiki/hacktricks.git` | `f9af277bf46a5ad8eaf9ab47555ddbeb64fe6661` |
| `ctf-wiki` | `https://github.com/ctf-wiki/ctf-wiki.git` | `e225ddfcd420a7f54a5940f47336ebdf8c29b875` |
| `volatility3` | `https://github.com/volatilityfoundation/volatility3.git` | `3fcb731e0ba5b6c4e90f19445a10f9da2bba02a4` |

Локальная копия HackTricks использует адрес проекта `HackTricks-wiki/hacktricks`; старый адрес `carlospolop/hacktricks` в прежних заметках устарел. Каталог `wordlists/` содержит ссылки на выбранные словари из `05_REPOS/SecLists/`; не перемещай одну папку отдельно, иначе относительные ссылки могут перестать работать.

## Инструменты

Загрузить переменные среды проекта:

```bash
cd /home/zuck/ico2027
source scripts/local_tools_env.sh
command -v gobuster
command -v yara
command -v zsteg
command -v ghidra
command -v ROPgadget
command -v checksec
command -v tshark
command -v wireshark
command -v sqlite3
command -v volatility3
```

Фактическое состояние при проверке:

- `gobuster`, `yara`, `zsteg`, `ghidra` — доступны как локальные инструменты проекта после `source scripts/local_tools_env.sh`.
- `ROPgadget` и `checksec` доступны в пользовательском PATH.
- `tshark`, `wireshark`, `sqlite3`, `file`, `strings`, `xxd`, `readelf`, `objdump`, `gdb`, `strace`, `ltrace`, `curl`, `wget`, `nc`, `tar`, `unzip`, `7z`, `sha256sum`, `binwalk`, `exiftool`, `ffmpeg` находятся в текущей системе.
- Команда `volatility3` в PATH отсутствует. Используй `scripts/vol.py`, который запускает исходный checkout через `.venv` и хранит кэш в проекте. Проверены CLI, plugin help и `frameworkinfo.FrameworkInfo` без дампа; дампа памяти для полноценного анализа в проекте нет.
- `hexdump` в PATH отсутствует; используй доступные `xxd` или `od`.
- Локальную установку CyberChef не нашли.
- Ghidra запускается из локальной установки, но здесь GUI/headless запуск не проверялся успешно: нужен подходящий JDK и, для GUI, рабочий графический сеанс.
- `ImHex` и Detect It Easy есть в распакованных материалах проекта; запуск графической оболочки ImHex в безоконной сессии не подтвердился.

Установка программ в систему через APT не выполнялась. Пакетные архивы, использованные при локальной подготовке, сохранены в `11_INSTALLERS/packages/`. Не удаляй этот каталог без необходимости.

## Материалы ICO

- Репозиторий `ico-2027/` содержит правила, writeup и связанные изображения, но сами бинарники и некоторые медиа задач находятся по внешней ссылке, указанной в локальном README. Не считай их скачанными.
- `05_REPOS/ico-tasks/` содержит описания ICO 2025 и четыре локальных ZIP-архива: `finals/14/2025-ICO-Q12-capturedData.zip`, `finals/15/2025-ICO-Q6-ping.zip`, `finals/17/2025-ICO-Q17.zip`, `finals/18/2025-ICO-Q18-reverseExe.zip`. Не все файлы, на которые ссылаются описания, входят в checkout.
- Существующие `ico-2027.bundle`, `ICO2027_PREP_PACK.zip` и резервные архивы сохранены.

## Материалы для обучения

Созданы русскоязычные `TRAIN_MANUAL.md`, `TOOL_INDEX.md`, `SCRIPT_INDEX.md`, `5H_TRAINING_PLAN.md`, `1H_CRASH_COURSE.md`, `MEMORIZATION.md` и `VIDEO_INDEX.md`. Каталог `09_VIDEOS/` проверен командой `find 09_VIDEOS -type f`; файлов там нет. Список в `VIDEO_INDEX.md` содержит онлайн-ссылки и не утверждает, что видео скачаны.

## Windows-инструменты

`x64dbg` и PE-bear — программы для Windows; их установщики в `11_INSTALLERS/` не обнаружены. Используй Windows-хост и официальные страницы проектов, если они нужны. Linux-версия Ghidra и другие перечисленные локальные инструменты не относятся к Windows-only.

## Проверка документации и скриптов

Выполнены проверки после правок документации:

```bash
python3 -m compileall -q scripts
find scripts -type f -name '*.sh' -print0 | xargs -0 -n1 bash -n
source scripts/local_tools_env.sh
bash scripts/offline_test.sh
find 09_VIDEOS -type f
```

Компиляция Python, проверка синтаксиса shell, `pip check` и `offline_test.sh` завершились успешно. В `scripts/` — 37 файлов первого уровня и 96 Python/shell-файлов во всех подпапках; `SCRIPT_INDEX.md` упоминает все 96. Отдельная проверка локальных Markdown-ссылок в документации и основных README ранее не находила битых ссылок.

Доступность здесь означает, что команда находится в PATH после загрузки среды; это не подтверждает проверку каждой функции. Ghidra найдена через локальный PATH, но интерфейс/бинарник задачи не запускались. Команда `volatility3` отсутствует в PATH, но `scripts/vol.py` запускает checkout через `.venv`; проверены `-h`, plugin help и безопасный `frameworkinfo.FrameworkInfo` без дампа. `hexdump` отсутствует; применяй `xxd`/`od`.

## Быстрое начало офлайн-работы

```bash
cd /home/zuck/ico2027
source scripts/local_tools_env.sh
source .venv/bin/activate
bash scripts/offline_test.sh
```

Чтобы запустить Ghidra headless, в прежней настройке применялись локальная JDK и каталог кэша проекта. Сначала проверь существование указанного JDK:

```bash
ls .local/app-root/usr/lib/jvm/java-25-openjdk-amd64/bin/java
```

Команда для Volatility 3 из checkout, если зависимости доступны:

```bash
scripts/vol.py -h
scripts/vol.py frameworkinfo.FrameworkInfo
scripts/vol.py -f MEMORY windows.info
```

Если команда не работает, запиши конкретную ошибку импорта/зависимости. Не подменяй её утверждением, что программа установлена в PATH.

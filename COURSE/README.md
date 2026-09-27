# ICO 2027 — навигация по курсу

Единая стартовая точка для существующих материалов проекта. Здесь только указатели: исходные документы, задания, scripts и репозитории не перемещаются и не копируются.

## START HERE

- [Начни прямо сейчас](00_START/README.md)
- [Исходный START_HERE](../docs/START_HERE.md)
- [Практический повтор за 1 час](../docs/1H_CRASH_COURSE.md)
- [План практики на 5–6 часов](../docs/5H_TRAINING_PLAN.md)
- [Отмечай прогресс](PROGRESS.md)

## Рекомендуемый порядок

1. Linux и основы работы с файлами.
2. Reverse и основы анализа ELF/PE.
3. Pwn: от защит бинарника до базовых примитивов.
4. Forensics и Network.
5. Crypto, Web, Stego и OSINT.
6. Смешанные задачи: ICO workflow и повторение.
7. Решай mini-CTF по мере прохождения блоков, затем переходи к локальным ICO задачам.

## Категории

- [Linux и базовая работа](01_LINUX/README.md) — темы TRAIN_MANUAL 01, 02, 03, 04, 05, 06, 07, 08.
- [Reverse Engineering](02_REVERSE/README.md) — темы TRAIN_MANUAL 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47.
- [Pwn и эксплуатация](03_PWN/README.md) — темы TRAIN_MANUAL 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58.
- [Forensics и анализ артефактов](04_FORENSICS/README.md) — темы TRAIN_MANUAL 05, 07, 08, 20, 21, 22, 24, 25, 59, 60, 61.
- [Сети и PCAP](05_NETWORK/README.md) — темы TRAIN_MANUAL 26, 27, 28, 29, 30, 31.
- [Криптография и кодировки](06_CRYPTO/README.md) — темы TRAIN_MANUAL 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19.
- [Web](07_WEB/README.md) — темы TRAIN_MANUAL 30, 32, 33, 34.
- [Стеганография](08_STEGO/README.md) — темы TRAIN_MANUAL 20, 21, 22, 23, 24, 25, 61.
- [OSINT и поиск по открытым данным](09_OSINT/README.md) — темы TRAIN_MANUAL 03, 04, 62.
- [Смешанные задачи и ICO workflow](10_MIXED/README.md) — темы TRAIN_MANUAL 00, 06, 07, 08, 15, 47, 59, 60, 62, 63, 64, 65, 66, 67.

## Практика и справочники

- [Все 12 заданий mini-CTF](../06_MINI_CTF/README.md)
- [Полное руководство — 68 тем](../docs/TRAIN_MANUAL.md)
- [Инструменты и способы запуска](../docs/TOOL_INDEX.md)
- [Scripts: назначение и примеры](../docs/SCRIPT_INDEX.md)
- [39 шпаргалок](../07_CHEATSHEETS/README.md)
- [Индекс видео](../docs/VIDEO_INDEX.md)
- [ICO 2025: локальные задачи](../05_REPOS/ico-tasks/README.md)
- [ICO 2027: локальные материалы](../ico-2027/README.md)
- [ICO 2027 qualifying writeup](../ico-2027/ico_qualifying_round/ico_ctf_writeup.md)
- [Быстрый индекс](QUICK_REFERENCE.md)
- [Маршрут, если застрял](WHEN_STUCK.md)

## Быстрый переход к инструменту

Ищи программу в [TOOL_INDEX](../docs/TOOL_INDEX.md) (статус установки там указывается отдельно), скрипт — в [SCRIPT_INDEX](../docs/SCRIPT_INDEX.md). Для локальной оболочки сначала выполни `source scripts/local_tools_env.sh`.

## Если застрял

1. Запиши точный путь к входному файлу и результат `file`.
2. Открой [диагностические маршруты](WHEN_STUCK.md) и соответствующую тему руководства.
3. Проверь команды и статус установки в TOOL_INDEX.
4. Запусти только относящийся к задаче script из SCRIPT_INDEX.
5. Проверь условие mini-CTF; writeup читай после собственной попытки.
6. Зафиксируй гипотезу, проверку и наблюдение в [прогрессе](PROGRESS.md).

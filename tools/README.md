# Локальные программы проекта

`tools/` не содержит дубликатов бинарников: команды установлены в системном PATH или распакованы в `.local/`. Перед использованием программ проекта загрузи их окружение:

    cd /home/zuck/ico2027
    source scripts/local_tools_env.sh
    command -v gobuster yara zsteg ghidra jq

Проверь конкретную команду через `docs/TOOL_INDEX.md`. Для Python-библиотек активируй `.venv`; для Volatility используй `scripts/vol.py`. Отсутствующие `ncat`, `masscan`, `feroxbuster`, `ropper`, `gef`, `pwndbg`, `docker` и `volatility3` как отдельную PATH-команду имеют задокументированные локальные альтернативы в справочнике.

Не копируй сюда второй экземпляр уже установленной программы. Установочные пакеты, доступные для офлайн-повторной установки, лежат в `11_INSTALLERS/`; Python wheels — в `10_WHEELS/`.

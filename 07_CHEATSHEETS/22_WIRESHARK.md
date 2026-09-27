# Wireshark

## Назначение

Интерактивный разбор PCAP.

## Основные команды и примеры

wireshark CAPTURE
# display filters: dns | http | tcp.stream eq 0 | frame contains "flag"

## Полезные варианты и ключи

Follow TCP Stream; Statistics → Conversations/Endpoints; display filters не удаляют пакеты из файла.

## Типичные ошибки

Wireshark GUI может быть недоступен в headless WSL; используй tshark как локальную альтернативу.

## Что проверить в CTF

Запиши фильтр, номер пакета и поток, а не только скриншот.

## Материалы проекта

../docs/TRAIN_MANUAL.md (27); ../docs/TOOL_INDEX.md

## Рабочая заметка

Скопируй команду и её вывод в заметки вместе с путём к входному файлу. Перед выводом проверь, что результат повторяется на том же входе и не зависит от случайного состояния оболочки.

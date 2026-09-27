# Powershell

## Назначение

Минимальная навигация и анализ Windows-артефактов в PowerShell.

## Основные команды и примеры

Get-ChildItem -Force
Get-FileHash .\sample.exe -Algorithm SHA256
Get-Content .\log.txt | Select-String -Pattern "error|flag"
Get-Command Get-FileHash

## Полезные варианты и ключи

-Recurse: обход подкаталогов; -Filter: ограничить файлы; -Encoding: читать текст с явной кодировкой.

## Типичные ошибки

PowerShell quoting отличается от Bash; не запускай неизвестные .ps1 и не меняй ExecutionPolicy без нужды.

## Что проверить в CTF

Сверь время/путь/хеш и сохраняй исходные события.

## Материалы проекта

../docs/TRAIN_MANUAL.md; ../docs/COMMAND_INDEX.md

## Рабочая заметка

Скопируй команду и её вывод в заметки вместе с путём к входному файлу. Перед выводом проверь, что результат повторяется на том же входе и не зависит от случайного состояния оболочки.

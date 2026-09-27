# Справочник команд — 554 примера

Команды оставлены без изменений, чтобы их можно было копировать. Подпись после тире указывает тему команды. Часть строк относится к первоначальной онлайн-настройке; перед выполнением проверяй `OFFLINE_STATUS.md`, текущий путь и наличие инструмента. Не запускай команды изменения/удаления данных без понимания последствий.


1. `pwd` — WSL/файловая система
1. `ls -lah` — WSL/файловая система
1. `find . -maxdepth 2 -type f | sort` — WSL/файловая система
1. `du -sh .` — WSL/файловая система
1. `df -h` — WSL/файловая система
1. `free -h` — WSL/файловая система
1. `uname -a` — WSL/файловая система
1. `cat /etc/os-release` — WSL/файловая система
1. `arch` — WSL/файловая система
1. `nproc` — WSL/файловая система
1. `echo $SHELL` — WSL/файловая система
1. `echo $PATH` — WSL/файловая система
1. `which python3` — WSL/файловая система
1. `python3 --version` — WSL/файловая система
1. `git --version` — WSL/файловая система
1. `curl --version` — WSL/файловая система
1. `stat FILE` — WSL/файловая система
1. `file FILE` — WSL/файловая система
1. `sha256sum FILE` — WSL/файловая система
1. `wc -c FILE` — WSL/файловая система
2. `ip addr` — Сеть/установка пакетов
2. `ip route` — Сеть/установка пакетов
2. `cat /etc/resolv.conf` — Сеть/установка пакетов
2. `getent hosts github.com` — Сеть/установка пакетов
2. `getent hosts pypi.org` — Сеть/установка пакетов
2. `getent hosts rubygems.org` — Сеть/установка пакетов
2. `curl -I https://www.kali.org` — Сеть/установка пакетов
2. `curl -I https://pypi.org` — Сеть/установка пакетов
2. `curl -I https://rubygems.org` — Сеть/установка пакетов
2. `sudo apt update` — Сеть/установка пакетов
2. `apt-cache policy python3-venv` — Сеть/установка пакетов
2. `apt-cache search python3-pwntools` — Сеть/установка пакетов
2. `sudo apt install -y python3-full python3-venv python3-pip python3-dev build-essential` — Сеть/установка пакетов
2. `sudo apt install -y file binutils gdb` — Сеть/установка пакетов
2. `sudo apt install -y ffmpeg sox imagemagick` — Сеть/установка пакетов
2. `sudo apt install -y tshark tcpdump` — Сеть/установка пакетов
2. `sudo apt install -y exiftool p7zip-full unzip zip` — Сеть/установка пакетов
2. `sudo apt install -y jq sqlite3` — Сеть/установка пакетов
2. `wsl --shutdown` — Сеть/установка пакетов
2. `ipconfig /flushdns` — Сеть/установка пакетов
3. `python3 -m venv ~/ico2027/.venv` — Python/пакеты и виртуальное окружение
3. `source ~/ico2027/.venv/bin/activate` — Python/пакеты и виртуальное окружение
3. `which python` — Python/пакеты и виртуальное окружение
3. `python --version` — Python/пакеты и виртуальное окружение
3. `python -m pip --version` — Python/пакеты и виртуальное окружение
3. `python -m pip install -U pip setuptools wheel` — Python/пакеты и виртуальное окружение
3. `python -m pip install pwntools` — Python/пакеты и виртуальное окружение
3. `python -m pip install scapy` — Python/пакеты и виртуальное окружение
3. `python -m pip install pycryptodome cryptography` — Python/пакеты и виртуальное окружение
3. `python -m pip install sympy z3-solver` — Python/пакеты и виртуальное окружение
3. `python -m pip install requests httpx` — Python/пакеты и виртуальное окружение
3. `python -m pip install beautifulsoup4 lxml` — Python/пакеты и виртуальное окружение
3. `python -m pip install dpkt` — Python/пакеты и виртуальное окружение
3. `python -m pip install pyelftools pefile lief` — Python/пакеты и виртуальное окружение
3. `python -m pip install capstone unicorn keystone-engine` — Python/пакеты и виртуальное окружение
3. `python -m pip install construct bitstring` — Python/пакеты и виртуальное окружение
3. `python -m pip install python-magic Pillow` — Python/пакеты и виртуальное окружение
3. `python -m pip install numpy scipy` — Python/пакеты и виртуальное окружение
3. `python -m pip install oletools olefile msoffcrypto-tool` — Python/пакеты и виртуальное окружение
3. `python -m pip install tqdm rich PyJWT` — Python/пакеты и виртуальное окружение
4. `mkdir -p ~/ico2027/10_WHEELS` — Офлайн-пакеты Python
4. `python -m pip freeze > ~/ico2027/10_WHEELS/requirements-online.txt` — Офлайн-пакеты Python
4. `python -m pip download -d ~/ico2027/10_WHEELS -r ~/ico2027/10_WHEELS/requirements-online.txt` — Офлайн-пакеты Python
4. `find ~/ico2027/10_WHEELS -type f | wc -l` — Офлайн-пакеты Python
4. `du -sh ~/ico2027/10_WHEELS` — Офлайн-пакеты Python
4. `sha256sum ~/ico2027/10_WHEELS/* > ~/ico2027/10_WHEELS/SHA256SUMS.txt` — Офлайн-пакеты Python
4. `sha256sum -c ~/ico2027/10_WHEELS/SHA256SUMS.txt` — Офлайн-пакеты Python
4. `python -m venv /tmp/ico-offline-test` — Офлайн-пакеты Python
4. `source /tmp/ico-offline-test/bin/activate` — Офлайн-пакеты Python
4. `python -m pip install --no-index --find-links ~/ico2027/10_WHEELS -r ~/ico2027/10_WHEELS/requirements-online.txt` — Офлайн-пакеты Python
4. `python -m pip check` — Офлайн-пакеты Python
4. `deactivate` — Офлайн-пакеты Python
4. `rm -rf /tmp/ico-offline-test` — Офлайн-пакеты Python
4. `python -m pip cache dir` — Офлайн-пакеты Python
4. `python -m pip cache list | head` — Офлайн-пакеты Python
4. `python -m pip show pwntools` — Офлайн-пакеты Python
4. `python -m pip list` — Офлайн-пакеты Python
4. `tar -czf ~/ico2027/99_BACKUP/wheels.tar.gz -C ~/ico2027 10_WHEELS` — Офлайн-пакеты Python
4. `sha256sum ~/ico2027/99_BACKUP/wheels.tar.gz` — Офлайн-пакеты Python
5. `git config --global user.name CTF` — Git/репозитории
5. `git config --global user.email ctf@example.invalid` — Git/репозитории
5. `git clone https://github.com/herachxx/ico-2027.git ~/ico2027/05_REPOS/ico-2027` — Git/репозитории
5. `git -C ~/ico2027/05_REPOS/ico-2027 status` — Git/репозитории
5. `git -C ~/ico2027/05_REPOS/ico-2027 log --oneline -10` — Git/репозитории
5. `git -C ~/ico2027/05_REPOS/ico-2027 remote -v` — Git/репозитории
5. `git -C ~/ico2027/05_REPOS/ico-2027 pull` — Git/репозитории
5. `git clone https://github.com/bysmaks/ico-tasks.git ~/ico2027/05_REPOS/ico-tasks` — Git/репозитории
5. `git clone https://github.com/Gallopsled/pwntools.git ~/ico2027/05_REPOS/pwntools` — Git/репозитории
5. `git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git ~/ico2027/05_REPOS/PayloadsAllTheThings` — Git/репозитории
5. `git clone https://github.com/danielmiessler/SecLists.git ~/ico2027/05_REPOS/SecLists` — Git/репозитории
5. `git clone https://github.com/carlospolop/hacktricks.git ~/ico2027/05_REPOS/hacktricks` — Git/репозитории
5. `git clone https://github.com/ctf-wiki/ctf-wiki.git ~/ico2027/05_REPOS/ctf-wiki` — Git/репозитории
5. `git clone https://github.com/volatilityfoundation/volatility3.git ~/ico2027/05_REPOS/volatility3` — Git/репозитории
5. `find ~/ico2027/05_REPOS -maxdepth 2 -type d | sort` — Git/репозитории
5. `du -sh ~/ico2027/05_REPOS/*` — Git/репозитории
5. `git -C ~/ico2027/05_REPOS/ico-tasks log --oneline -5` — Git/репозитории
5. `git -C ~/ico2027/05_REPOS/pwntools log --oneline -5` — Git/репозитории
5. `tar -czf ~/ico2027/99_BACKUP/repos.tar.gz -C ~/ico2027/05_REPOS .` — Git/репозитории
6. `file FILE` — Первичная проверка файлов
6. `stat FILE` — Первичная проверка файлов
6. `ls -lah FILE` — Первичная проверка файлов
6. `xxd -g 1 -l 128 FILE` — Первичная проверка файлов
6. `xxd -g 1 FILE | less` — Первичная проверка файлов
6. `strings -a -n 5 FILE | less` — Первичная проверка файлов
6. `strings -a -el FILE | less` — Первичная проверка файлов
6. `strings -a -n 8 FILE | grep -Ei 'flag|ico|key|pass|token|http|user'` — Первичная проверка файлов
6. `binwalk FILE` — Первичная проверка файлов
6. `binwalk -e FILE` — Первичная проверка файлов
6. `exiftool FILE` — Первичная проверка файлов
6. `identify FILE` — Первичная проверка файлов
6. `sha256sum FILE` — Первичная проверка файлов
6. `md5sum FILE` — Первичная проверка файлов
6. `cmp FILE COPY` — Первичная проверка файлов
6. `hexdump -C FILE | head` — Первичная проверка файлов
6. `od -Ax -tx1z -N 256 FILE` — Первичная проверка файлов
6. `wc -c FILE` — Первичная проверка файлов
6. `tail -c 128 FILE | xxd` — Первичная проверка файлов
6. `find . -type f -exec file {} \;` — Первичная проверка файлов
7. `echo SGVsbG8= | base64 -d` — Кодировки
7. `echo 48656c6c6f | xxd -r -p` — Кодировки
7. `echo -n hello | xxd -p` — Кодировки
7. `echo -n hello | base64` — Кодировки
7. `python3 -c "import base64; print(base64.b64decode("SGVsbG8=").decode())"` — Кодировки
7. `python3 -c "import base64; print(base64.b32decode("JBSWY3DP").decode())"` — Кодировки
7. `python3 -c "import base64; print(base64.b85decode("NM&qnZ!92").decode())"` — Кодировки
7. `python3 -c "import urllib.parse; print(urllib.parse.unquote("%69%63%6f"))"` — Кодировки
7. `python3 -c "import codecs; print(codecs.decode("uryyb","rot_13"))"` — Кодировки
7. `tr 'A-Za-z' 'N-ZA-Mn-za-m' <<< uryyb` — Кодировки
7. `printf hello | od -An -tu1` — Кодировки
7. `grep -Eo '[A-Za-z0-9+/=]{12,}' FILE` — Кодировки
7. `grep -Eo '[0-9a-fA-F]{16,}' FILE` — Кодировки
7. `tr -d '\n\r ' < encoded.txt | base64 -d` — Кодировки
7. `python3 -c "print(bytes.fromhex("68656c6c6f"))"` — Кодировки
7. `python3 -c "print(int("deadbeef",16))"` — Кодировки
7. `python3 -c "print(hex(3735928559))"` — Кодировки
7. `python3 -c "print(bin(42))"` — Кодировки
7. `python3 -c "print(int("101010",2))"` — Кодировки
7. `python3 -c "print("hello"[::-1])"` — Кодировки
8. `pngcheck -v image.png` — Стеганография/изображения
8. `zsteg -a image.png` — Стеганография/изображения
8. `zsteg -E b4,g,lsb,xy image.png > extracted.bin` — Стеганография/изображения
8. `steghide info photo.jpg` — Стеганография/изображения
8. `steghide extract -sf photo.jpg` — Стеганография/изображения
8. `exiftool photo.jpg` — Стеганография/изображения
8. `binwalk image.png` — Стеганография/изображения
8. `binwalk -e image.png` — Стеганография/изображения
8. `foremost -i image.png -o carved` — Стеганография/изображения
8. `strings image.png | less` — Стеганография/изображения
8. `xxd image.png | tail` — Стеганография/изображения
8. `identify image.png` — Стеганография/изображения
8. `python3 scripts/png_chunks.py image.png` — Стеганография/изображения
8. `python3 scripts/lsb_image.py image.png` — Стеганография/изображения
8. `convert image.png -channel R -separate red.png` — Стеганография/изображения
8. `convert image.png -channel G -separate green.png` — Стеганография/изображения
8. `convert image.png -channel B -separate blue.png` — Стеганография/изображения
8. `exiftool -gpslatitude -gpslongitude photo.jpg` — Стеганография/изображения
8. `exiftool -comment -description photo.jpg` — Стеганография/изображения
8. `sha256sum image.png` — Стеганография/изображения
9. `file audio.wav` — Аудио
9. `ffprobe audio.wav` — Аудио
9. `ffmpeg -i audio.wav` — Аудио
9. `sox audio.wav -n stat` — Аудио
9. `sox audio.wav -n spectrogram -o spectrogram.png` — Аудио
9. `ffmpeg -i audio.wav -lavfi showspectrumpic=s=1600x900 spectrogram.png` — Аудио
9. `strings audio.wav | less` — Аудио
9. `binwalk audio.wav` — Аудио
9. `xxd -l 64 audio.wav` — Аудио
9. `xxd -s -64 audio.wav` — Аудио
9. `ffmpeg -i audio.wav -ac 1 mono.wav` — Аудио
9. `ffmpeg -i audio.wav -ar 44100 normalized.wav` — Аудио
9. `sox audio.wav reversed.wav reverse` — Аудио
9. `sox audio.wav slowed.wav tempo 0.5` — Аудио
9. `ffmpeg -i audio.wav -af volumedetect -f null /dev/null` — Аудио
9. `python3 scripts/audio_report.py audio.wav` — Аудио
9. `file spectrogram.png` — Аудио
9. `zsteg -a spectrogram.png` — Аудио
9. `cp audio.wav working.wav` — Аудио
9. `sha256sum audio.wav` — Аудио
10. `capinfos traffic.pcap` — сетевые захваты PCAP
10. `tshark -r traffic.pcap` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -q -z io,phs` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -Y dns` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -Y dns -T fields -e dns.qry.name` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -Y http` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -Y 'http.request'` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -Y 'tcp.stream eq 0'` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -z follow,tcp,ascii,0` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -Y tls.handshake` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -Y icmp` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -T fields -e frame.number -e ip.src -e ip.dst -e tcp.dstport` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -Y dns -T fields -e dns.qry.name | sort -u` — сетевые захваты PCAP
10. `tcpdump -nn -r traffic.pcap` — сетевые захваты PCAP
10. `python3 scripts/pcap_summary.py traffic.pcap` — сетевые захваты PCAP
10. `python3 scripts/dns_extract.py traffic.pcap` — сетевые захваты PCAP
10. `python3 scripts/dns_join_decode.py traffic.pcap` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -T fields -e tcp.stream | sort -nu` — сетевые захваты PCAP
10. `tshark -r traffic.pcap -Y 'tcp.len > 0'` — сетевые захваты PCAP
10. `sha256sum traffic.pcap` — сетевые захваты PCAP
11. `file ./challenge` — ELF/обратная разработка
11. `checksec --file=./challenge` — ELF/обратная разработка
11. `readelf -h ./challenge` — ELF/обратная разработка
11. `readelf -S ./challenge` — ELF/обратная разработка
11. `readelf -s ./challenge` — ELF/обратная разработка
11. `readelf -r ./challenge` — ELF/обратная разработка
11. `readelf -l ./challenge` — ELF/обратная разработка
11. `objdump -d -M intel ./challenge | less` — ELF/обратная разработка
11. `objdump -D -M intel ./challenge | less` — ELF/обратная разработка
11. `objdump -s ./challenge | less` — ELF/обратная разработка
11. `nm -C ./challenge | less` — ELF/обратная разработка
11. `strings -a ./challenge | less` — ELF/обратная разработка
11. `ldd ./challenge` — ELF/обратная разработка
11. `./challenge` — ELF/обратная разработка
11. `gdb ./challenge` — ELF/обратная разработка
11. `gdb -q ./challenge -ex 'info functions' -ex quit` — ELF/обратная разработка
11. `gdb -q ./challenge -ex 'disassemble main' -ex quit` — ELF/обратная разработка
11. `objdump -d -M intel ./challenge | grep -E 'call|cmp|test|jmp'` — ELF/обратная разработка
11. `python3 scripts/elf_triage.py ./challenge` — ELF/обратная разработка
11. `sha256sum ./challenge` — ELF/обратная разработка
12. `gdb -q ./challenge` — GDB
12. `set disassembly-flavor intel` — GDB
12. `start` — GDB
12. `run` — GDB
12. `break main` — GDB
12. `break *0x401000` — GDB
12. `info registers` — GDB
12. `x/16gx $rsp` — GDB
12. `x/32bx $rsp` — GDB
12. `x/s $rdi` — GDB
12. `x/20i $rip` — GDB
12. `disassemble main` — GDB
12. `bt` — GDB
12. `info frame` — GDB
12. `continue` — GDB
12. `stepi` — GDB
12. `nexti` — GDB
12. `finish` — GDB
12. `set pagination off` — GDB
12. `info files` — GDB
13. `python3 -c 'from pwn import *; print(cyclic(100))'` — Pwn/ROP
13. `python3 -c 'from pwn import *; print(cyclic_find(0x6161616c))'` — Pwn/ROP
13. `python3 -c 'from pwn import *; print(p64(0x401234))'` — Pwn/ROP
13. `python3 -c 'from pwn import *; print(p32(0x12345678))'` — Pwn/ROP
13. `ROPgadget --binary ./challenge` — Pwn/ROP
13. `ROPgadget --binary ./challenge --only 'pop|ret'` — Pwn/ROP
13. `ropper --file ./challenge --search 'pop rdi; ret'` — Pwn/ROP
13. `nm -an ./challenge | grep -E 'win|flag|admin'` — Pwn/ROP
13. `strings ./challenge | grep -Ei 'flag|admin|secret'` — Pwn/ROP
13. `python3 scripts/rop_template.py` — Pwn/ROP
13. `python3 scripts/format_string_template.py` — Pwn/ROP
13. `printf '%p.%p.%p.%p.%p.%p.%p.%p\n' | ./challenge` — Pwn/ROP
13. `python3 -c 'from pwn import *; print(fmtstr_payload(6,{0x40407c:1},write_size="byte"))'` — Pwn/ROP
13. `python3 scripts/offset_finder.py --length 300` — Pwn/ROP
13. `python3 scripts/pack.py 0x401234` — Pwn/ROP
13. `python3 scripts/leak_parser.py leak.txt` — Pwn/ROP
13. `checksec --file=./challenge` — Pwn/ROP
13. `gdb -q ./challenge` — Pwn/ROP
13. `info registers rdi rsi rdx rsp rbp rip` — Pwn/ROP
14. `curl -I https://TARGET/` — Веб/HTTP
14. `curl -sk https://TARGET/` — Веб/HTTP
14. `curl -sk -i https://TARGET/` — Веб/HTTP
14. `curl -skL https://TARGET/` — Веб/HTTP
14. `curl -sk https://TARGET/robots.txt` — Веб/HTTP
14. `curl -sk https://TARGET/sitemap.xml` — Веб/HTTP
14. `curl -sk https://TARGET/.well-known/security.txt` — Веб/HTTP
14. `curl -sk https://TARGET/api` — Веб/HTTP
14. `curl -sk https://TARGET/wp-json/` — Веб/HTTP
14. `curl -sk https://TARGET/wp-json/wp/v2/users` — Веб/HTTP
14. `curl -sk -X OPTIONS https://TARGET/` — Веб/HTTP
14. `curl -sk -c cookies.txt https://TARGET/` — Веб/HTTP
14. `curl -sk -b cookies.txt https://TARGET/private` — Веб/HTTP
14. `curl -sk -H 'Content-Type: application/json' -d '{"x":"test"}' https://TARGET/api` — Веб/HTTP
14. `curl -sk https://TARGET/ | tee page.html` — Веб/HTTP
14. `grep -Eo 'https?://[^" ]+' page.html` — Веб/HTTP
14. `grep -Ei 'api|token|debug|admin|flag|secret' page.html` — Веб/HTTP
14. `python3 scripts/web_probe.py https://TARGET/` — Веб/HTTP
14. `python3 scripts/header_report.py https://TARGET/` — Веб/HTTP
14. `python3 scripts/form_parser.py page.html` — Веб/HTTP
15. `curl -sk -X POST https://TARGET/login --data-urlencode "username=' OR 1=1-- -" --data-urlencode 'password=x'` — SQL/API
15. `curl -sk 'https://TARGET/item?id=1'` — SQL/API
15. `curl -sk 'https://TARGET/item?id=1%27'` — SQL/API
15. `curl -sk 'https://TARGET/item?id=1%20OR%201%3D1'` — SQL/API
15. `curl -sk -G https://TARGET/search --data-urlencode 'q=test'` — SQL/API
15. `sqlmap -u 'https://TARGET/item?id=1' --batch` — SQL/API
15. `sqlmap -u 'https://TARGET/item?id=1' --dbs --batch` — SQL/API
15. `sqlmap -u 'https://TARGET/item?id=1' -D DB --tables --batch` — SQL/API
15. `sqlmap -u 'https://TARGET/item?id=1' -D DB -T TABLE --columns --batch` — SQL/API
15. `curl -sk https://TARGET/login -o response.html` — SQL/API
15. `grep -Ei 'sql|sqlite|mysql|postgres|error|exception' response.html` — SQL/API
15. `jq . response.json` — SQL/API
15. `jq '.. | strings' response.json` — SQL/API
15. `python3 scripts/json_paths.py response.json` — SQL/API
15. `curl -sk -H 'Content-Type: application/json' -d '{}' https://TARGET/api` — SQL/API
15. `curl -sk -X OPTIONS https://TARGET/api` — SQL/API
15. `file database.db` — SQL/API
15. `sqlite3 database.db '.tables'` — SQL/API
15. `sqlite3 database.db '.schema'` — SQL/API
15. `sqlite3 database.db '.dump' > dump.sql` — SQL/API
16. `python3 -c "from hashlib import sha256; print(sha256(b"hello").hexdigest())"` — Криптография
16. `python3 -c "from hashlib import md5; print(md5(b"hello").hexdigest())"` — Криптография
16. `python3 -c "from hashlib import sha1; print(sha1(b"hello").hexdigest())"` — Криптография
16. `python3 -c "import hmac,hashlib; print(hmac.new(b"k",b"m",hashlib.sha256).hexdigest())"` — Криптография
16. `python3 -c "from криптография.Cipher import AES; print(AES.block_size)"` — Криптография
16. `python3 -c "from криптография.Util.number import inverse; print(inverse(3,11))"` — Криптография
16. `python3 -c "print(pow(3,-1,11))"` — Криптография
16. `python3 -c "print(pow(2,100,101))"` — Криптография
16. `python3 -c "import sympy as s; print(s.factorint(123456789))"` — Криптография
16. `python3 -c "from z3 import *; x=Int("x"); s=Solver(); s.add(x>10,x<20); print(s.check(),s.model())"` — Криптография
16. `python3 scripts/xor_singlebyte.py ciphertext.bin` — Криптография
16. `python3 scripts/lcg_solver.py 1 2 5` — Криптография
16. `python3 scripts/lcg_predict.py 1 5 3 -n 10` — Криптография
16. `python3 scripts/hash_report.py sample` — Криптография
16. `python3 scripts/hash_padding.py 18 20` — Криптография
16. `python3 scripts/length_extension_template.py` — Криптография
16. `python3 scripts/rsa_helpers.py 3233 17 2790` — Криптография
16. `python3 -c "import math; print(math.gcd(123,2**32))"` — Криптография
16. `python3 -c "print(2**32)"` — Криптография
16. `sha256sum sample` — Криптография
17. `python3 scripts/lcg_solver.py 1 2 5` — LCG/математика
17. `python3 scripts/lcg_predict.py 1 5 3 -n 20` — LCG/математика
17. `python3 -c "print(3591405241>>16)"` — LCG/математика
17. `python3 -c "print(3591405241&0xffff)"` — LCG/математика
17. `python3 -c "print(pow(3,-1,2**32))"` — LCG/математика
17. `python3 -c "print(2**16)"` — LCG/математика
17. `python3 -c "print(2**20)"` — LCG/математика
17. `python3 -c "print(2**24)"` — LCG/математика
17. `python3 -c "print((274874657*123456789+646369019)%(2**32))"` — LCG/математика
17. `python3 -c "print((6364136223846793005+1442695040888963407)&((1<<64)-1))"` — LCG/математика
17. `python3 -c "x=1; print((x>>24)&255)"` — LCG/математика
17. `python3 -c "print((1%7)+1)"` — LCG/математика
17. `python3 -c "def r(x,r): return ((x<<r)|(x>>(8-r)))&255; print(hex(r(0x12,3)))"` — LCG/математика
17. `python3 -c "def r(x,r): return ((x>>r)|(x<<(8-r)))&255; print(hex(r(0x91,3)))"` — LCG/математика
17. `python3 -c "print(hex(0xffffffff))"` — LCG/математика
17. `python3 -c "print(hex(0xffffffffffffffff))"` — LCG/математика
17. `python3 -c "import math; print(math.gcd(123,2**32))"` — LCG/математика
17. `python3 scripts/bruteforce_lowbits.py 54800` — LCG/математика
17. `python3 -c "print(65536)"` — LCG/математика
17. `python3 -c "print(2**32)"` — LCG/математика
18. `file sample.exe` — PE/Windows
18. `strings -a sample.exe | less` — PE/Windows
18. `strings -a -el sample.exe | less` — PE/Windows
18. `objdump -x sample.exe | less` — PE/Windows
18. `python3 scripts/pe_triage.py sample.exe` — PE/Windows
18. `python3 -c "import pefile; p=pefile.PE("sample.exe"); print([x.name for x in p.sections])"` — PE/Windows
18. `python3 -c "import pefile; p=pefile.PE("sample.exe"); print(hex(p.FILE_HEADER.Machine))"` — PE/Windows
18. `python3 -c "import pefile; p=pefile.PE("sample.exe"); print(hex(p.OPTIONAL_HEADER.ImageBase))"` — PE/Windows
18. `python3 -c "import pefile; p=pefile.PE("sample.exe"); print(hex(p.OPTIONAL_HEADER.AddressOfEntryPoint))"` — PE/Windows
18. `python3 -c "import pefile; p=pefile.PE("sample.exe"); print([d.dll for d in p.DIRECTORY_ENTRY_IMPORT])"` — PE/Windows
18. `exiftool sample.exe` — PE/Windows
18. `sha256sum sample.exe` — PE/Windows
18. `find . -iname '*.exe' -o -iname '*.dll'` — PE/Windows
18. `strings -a -el sample.exe | grep -Ei 'flag|http|pass|token'` — PE/Windows
18. `objdump -p sample.exe | grep -i dll` — PE/Windows
18. `objdump -p sample.exe | grep -i entry` — PE/Windows
18. `python3 -m pip show pefile` — PE/Windows
18. `python3 -m pip show lief` — PE/Windows
18. `rabin2 -I sample.exe` — PE/Windows
19. `vol.py -f memory.raw windows.info` — Форензика памяти
19. `vol.py -f memory.raw windows.pslist` — Форензика памяти
19. `vol.py -f memory.raw windows.pstree` — Форензика памяти
19. `vol.py -f memory.raw windows.cmdline` — Форензика памяти
19. `vol.py -f memory.raw windows.netscan` — Форензика памяти
19. `vol.py -f memory.raw windows.filescan` — Форензика памяти
19. `vol.py -f memory.raw windows.dlllist` — Форензика памяти
19. `strings -a memory.raw | grep -Ei 'flag|ico|http|password'` — Форензика памяти
19. `sha256sum memory.raw` — Форензика памяти
19. `file memory.raw` — Форензика памяти
19. `find . -iname '*.raw' -o -iname '*.dmp'` — Форензика памяти
19. `yara --version` — Форензика памяти
19. `python3 -m pip show volatility3` — Форензика памяти
19. `python3 -m pip list | grep -Ei 'volatility|pefile|yara'` — Форензика памяти
19. `foremost -i memory.raw -o carved` — Форензика памяти
19. `binwalk memory.raw` — Форензика памяти
19. `strings -a memory.raw | less` — Форензика памяти
19. `grep -aob 'ico{' memory.raw | head` — Форензика памяти
19. `xxd -l 256 memory.raw` — Форензика памяти
19. `sha256sum memory.raw > memory.sha256` — Форензика памяти
20. `find ~/ico2027/05_REPOS/SecLists -maxdepth 2 -type f | head` — Словари/тестирование ввода
20. `find ~/ico2027/05_REPOS/SecLists -iname '*password*' | head` — Словари/тестирование ввода
20. `find ~/ico2027/05_REPOS/SecLists -iname '*directory*' | head` — Словари/тестирование ввода
20. `find /usr/share/wordlists -type f 2>/dev/null` — Словари/тестирование ввода
20. `ls -lh /usr/share/wordlists/rockyou.txt.gz 2>/dev/null` — Словари/тестирование ввода
20. `sudo gzip -dk /usr/share/wordlists/rockyou.txt.gz` — Словари/тестирование ввода
20. `wc -l /usr/share/wordlists/rockyou.txt` — Словари/тестирование ввода
20. `head -20 /usr/share/wordlists/rockyou.txt` — Словари/тестирование ввода
20. `grep -i '^password$' /usr/share/wordlists/rockyou.txt` — Словари/тестирование ввода
20. `sort -u words.txt > words.unique.txt` — Словари/тестирование ввода
20. `ffuf -u https://TARGET/FUZZ -w WORDLIST` — Словари/тестирование ввода
20. `ffuf -u https://TARGET/FUZZ -w WORDLIST -fc 404` — Словари/тестирование ввода
20. `ffuf -u https://TARGET/FUZZ -w WORDLIST -fs 1234` — Словари/тестирование ввода
20. `gobuster dir -u https://TARGET -w WORDLIST` — Словари/тестирование ввода
20. `gobuster vhost -u https://TARGET -w WORDLIST` — Словари/тестирование ввода
20. `grep -Ei 'admin|login|api|debug|backup' words.txt` — Словари/тестирование ввода
20. `wc -l words.unique.txt` — Словари/тестирование ввода
20. `head -50 words.unique.txt` — Словари/тестирование ввода
20. `du -sh ~/ico2027/05_REPOS/SecLists` — Словари/тестирование ввода
20. `sha256sum words.unique.txt` — Словари/тестирование ввода
21. `7z l archive.zip` — Архивы
21. `7z x archive.zip -oout` — Архивы
21. `unzip -l archive.zip` — Архивы
21. `unzip archive.zip -d out` — Архивы
21. `tar -tf archive.tar` — Архивы
21. `tar -xf archive.tar -C out` — Архивы
21. `gzip -dc file.gz > file` — Архивы
21. `xz -dc file.xz > file` — Архивы
21. `strings archive.zip | grep -Ei 'flag|ico'` — Архивы
21. `find out -type f -exec file {} \;` — Архивы
21. `find out -type f -printf "%s %p\n" | sort -n` — Архивы
21. `sha256sum archive.zip` — Архивы
21. `zipinfo archive.zip | head` — Архивы
21. `7z t archive.zip` — Архивы
21. `7z l archive.7z` — Архивы
21. `7z x archive.7z -oout7z` — Архивы
21. `tar -czf output.tar.gz out/` — Архивы
21. `tar -tzf output.tar.gz` — Архивы
21. `find . -type f -size 0 -print` — Архивы
21. `du -sh out` — Архивы
22. `sha256sum sample > sample.sha256` — Данные/хеширование
22. `sha256sum -c sample.sha256` — Данные/хеширование
22. `find . -type f -print0 | sort -z | xargs -0 sha256sum > MANIFEST.sha256` — Данные/хеширование
22. `stat sample` — Данные/хеширование
22. `cp -a evidence evidence_work` — Данные/хеширование
22. `chmod -R a-w evidence` — Данные/хеширование
22. `mkdir -p 15_OUTPUT/case1` — Данные/хеширование
22. `script -a terminal.log` — Данные/хеширование
22. `exit` — Данные/хеширование
22. `tee notes.txt` — Данные/хеширование
22. `cat notes.txt` — Данные/хеширование
22. `date -Is >> notes.txt` — Данные/хеширование
22. `sha256sum -c MANIFEST.sha256` — Данные/хеширование
22. `find . -type f -printf '%p\n' | sort > FILELIST.txt` — Данные/хеширование
22. `wc -l FILELIST.txt` — Данные/хеширование
22. `du -sh .` — Данные/хеширование
22. `find . -type f -size 0 -print` — Данные/хеширование
22. `find . -name '*.part' -o -name '*.crdownload` — Данные/хеширование
22. `tar -czf evidence_work.tar.gz evidence_work/` — Данные/хеширование
22. `sha256sum evidence_work.tar.gz` — Данные/хеширование
23. `file database.db` — SQLite
23. `sqlite3 database.db '.tables'` — SQLite
23. `sqlite3 database.db '.schema'` — SQLite
23. `sqlite3 database.db 'SELECT name FROM sqlite_master WHERE type="table";'` — SQLite
23. `sqlite3 database.db '.dump' > dump.sql` — SQLite
23. `sqlite3 database.db 'PRAGMA database_list;'` — SQLite
23. `sqlite3 database.db 'PRAGMA table_info(users);'` — SQLite
23. `sqlite3 database.db 'SELECT * FROM users LIMIT 20;'` — SQLite
23. `grep -Ei 'flag|ico|secret|token' dump.sql` — SQLite
23. `sqlite3 database.db 'SELECT sql FROM sqlite_master;'` — SQLite
23. `sqlite3 database.db '.indexes'` — SQLite
23. `sqlite3 database.db '.databases'` — SQLite
23. `cp database.db database_work.db` — SQLite
23. `sha256sum database.db` — SQLite
23. `strings database.db | grep -Ei 'flag|secret'` — SQLite
23. `xxd -l 64 database.db` — SQLite
23. `file dump.sql` — SQLite
23. `wc -l dump.sql` — SQLite
23. `du -sh database.db` — SQLite
23. `sqlite3 database_work.db ".tables"` — SQLite
24. `grep -Rni btoa .` — JavaScript
24. `grep -Rni atob .` — JavaScript
24. `grep -Rni charCodeAt .` — JavaScript
24. `grep -Rni fromCharCode .` — JavaScript
24. `grep -Rni reverse .` — JavaScript
24. `node --version` — JavaScript
24. `node -e 'console.log(Buffer.from("SGVsbG8=","base64").toString())'` — JavaScript
24. `grep -n <script page.html` — JavaScript
24. `grep -Eo 'src="[^"]+"' page.html` — JavaScript
24. `curl -sk https://TARGET/app.js -o app.js` — JavaScript
24. `grep -Ei 'api|token|flag|secret|debug' app.js` — JavaScript
24. `python3 scripts/base_decode.py encoded.txt` — JavaScript
24. `python3 scripts/rot13.py clue.txt` — JavaScript
24. `strings -a app.js | less` — JavaScript
24. `sha256sum app.js` — JavaScript
24. `wc -c app.js` — JavaScript
24. `head -50 app.js` — JavaScript
24. `tail -50 app.js` — JavaScript
24. `grep -Eo '/[A-Za-z0-9_./-]{2,}' app.js` — JavaScript
24. `grep -Ei 'eval|Function|fetch|XMLHttpRequest' app.js` — JavaScript
25. `ps aux` — Linux/процессы
25. `ps -ef` — Linux/процессы
25. `top -b -n 1 | head -30` — Linux/процессы
25. `ss -lntup` — Linux/процессы
25. `ss -plant` — Linux/процессы
25. `lsof -i -P -n` — Linux/процессы
25. `lsof FILE` — Linux/процессы
25. `id` — Linux/процессы
25. `whoami` — Linux/процессы
25. `groups` — Linux/процессы
25. `env | sort` — Linux/процессы
25. `printenv | sort` — Linux/процессы
25. `cat /proc/self/status` — Linux/процессы
25. `cat /proc/self/maps` — Linux/процессы
25. `readlink /proc/self/exe` — Linux/процессы
25. `find /tmp -maxdepth 2 -type f -ls` — Linux/процессы
25. `find /var/tmp -maxdepth 2 -type f -ls` — Linux/процессы
25. `find . -maxdepth 2 -type f -perm -111 -ls` — Linux/процессы
25. `getcap -r . 2>/dev/null` — Linux/процессы
25. `ldd ./challenge` — Linux/процессы
26. `git -C ~/ico2027/05_REPOS/ico-2027 grep -n 'Rev Zero'` — Практика/задачи ICO
26. `git -C ~/ico2027/05_REPOS/ico-2027 grep -n 'Wolf Protocol'` — Практика/задачи ICO
26. `git -C ~/ico2027/05_REPOS/ico-2027 grep -n 'Can you hear'` — Практика/задачи ICO
26. `git -C ~/ico2027/05_REPOS/ico-2027 grep -n 'Five Shards'` — Практика/задачи ICO
26. `git -C ~/ico2027/05_REPOS/ico-2027 grep -n 'NorthStar'` — Практика/задачи ICO
26. `git -C ~/ico2027/05_REPOS/ico-2027 grep -n 'Backdoor'` — Практика/задачи ICO
26. `git -C ~/ico2027/05_REPOS/ico-2027 grep -n 'PixelMart'` — Практика/задачи ICO
26. `git -C ~/ico2027/05_REPOS/ico-2027 grep -n 'VIP Club'` — Практика/задачи ICO
26. `git -C ~/ico2027/05_REPOS/ico-2027 grep -n 'Journal Operator'` — Практика/задачи ICO
26. `git -C ~/ico2027/05_REPOS/ico-2027 grep -n 'AEZAKMI'` — Практика/задачи ICO
26. `grep -Rni fmtstr_payload ~/ico2027/05_REPOS` — Практика/задачи ICO
26. `grep -Rni 'cyclic(' ~/ico2027/05_REPOS` — Практика/задачи ICO
26. `grep -Rni 'length extension' ~/ico2027/05_REPOS` — Практика/задачи ICO
26. `grep -Rni LCG ~/ico2027/05_REPOS` — Практика/задачи ICO
26. `grep -Rni spectrogram ~/ico2027/05_REPOS` — Практика/задачи ICO
26. `grep -Rni zsteg ~/ico2027/05_REPOS` — Практика/задачи ICO
26. `grep -Rni tshark ~/ico2027/05_REPOS` — Практика/задачи ICO
26. `grep -Rni checksec ~/ico2027/05_REPOS` — Практика/задачи ICO
26. `grep -Rni pwntools ~/ico2027/05_REPOS` — Практика/задачи ICO
26. `find ~/ico2027/05_REPOS -name '*.md' | sort | head -100` — Практика/задачи ICO
27. `find ~/ico2027 -type f -iname "*.mp4" -o -iname "*.mkv"` — Материалы для поездки/офлайн
27. `find ~/ico2027 -type f -iname "*.pdf"` — Материалы для поездки/офлайн
27. `find ~/ico2027 -type f -iname "*.html"` — Материалы для поездки/офлайн
27. `find ~/ico2027 -type f -iname "*.md" | wc -l` — Материалы для поездки/офлайн
27. `du -sh ~/ico2027/08_BOOKS ~/ico2027/09_VIDEOS` — Материалы для поездки/офлайн
27. `find ~/ico2027/11_INSTALLERS -type f -maxdepth 1 -ls` — Материалы для поездки/офлайн
27. `find ~/ico2027/07_CHEATSHEETS -type f -maxdepth 1 -ls` — Материалы для поездки/офлайн
27. `find ~/ico2027/01_WRITEUPS -type f -maxdepth 2 -ls` — Материалы для поездки/офлайн
27. `find ~/ico2027/05_REPOS/ico-2027 -type f | wc -l` — Материалы для поездки/офлайн
27. `find ~/ico2027/05_REPOS/ico-tasks -type f | wc -l` — Материалы для поездки/офлайн
27. `find ~/ico2027/10_WHEELS -type f | wc -l` — Материалы для поездки/офлайн
27. `find ~/ico2027/04_WORDLISTS -type f | wc -l` — Материалы для поездки/офлайн
27. `tar -czf ~/ico2027/99_BACKUP/train-materials.tar.gz -C ~/ico2027 01_WRITEUPS 07_CHEATSHEETS 08_BOOKS 09_VIDEOS` — Материалы для поездки/офлайн
27. `sha256sum ~/ico2027/99_BACKUP/train-materials.tar.gz` — Материалы для поездки/офлайн
27. `find ~/ico2027/09_VIDEOS -type f -printf "%s %p\n" | sort -n` — Материалы для поездки/офлайн
27. `find ~/ico2027/08_BOOKS -type f -printf "%s %p\n" | sort -n` — Материалы для поездки/офлайн
27. `find ~/ico2027/07_CHEATSHEETS -type f -printf "%s %p\n" | sort -n` — Материалы для поездки/офлайн
27. `du -sh ~/ico2027/99_BACKUP` — Материалы для поездки/офлайн
27. `find ~/ico2027 -type f -size 0 -print` — Материалы для поездки/офлайн
28. `tar -czf ~/ico2027/99_BACKUP/ico2027-full.tar.gz -C ~ ico2027` — Резервные копии
28. `sha256sum ~/ico2027/99_BACKUP/ico2027-full.tar.gz` — Резервные копии
28. `tar -tzf ~/ico2027/99_BACKUP/ico2027-full.tar.gz | head` — Резервные копии
28. `find ~/ico2027 -type f | wc -l` — Резервные копии
28. `find ~/ico2027 -type f -size 0 -print` — Резервные копии
28. `find ~/ico2027 -name '*.part' -o -name '*.crdownload` — Резервные копии
28. `du -sh ~/ico2027` — Резервные копии
28. `cp ~/ico2027/99_BACKUP/ico2027-full.tar.gz /mnt/c/Users/$USER/Desktop/ 2>/dev/null || true` — Резервные копии
28. `cp ~/ico2027/99_BACKUP/ico2027-full.tar.gz /mnt/c/Users/Public/ 2>/dev/null || true` — Резервные копии
28. `find ~/ico2027/99_BACKUP -type f -ls` — Резервные копии
28. `ls -lh ~/ico2027/99_BACKUP` — Резервные копии
28. `tar -tf ~/ico2027/99_BACKUP/repos.tar.gz | head 2>/dev/null || true` — Резервные копии
28. `tar -tf ~/ico2027/99_BACKUP/wheels.tar.gz | head 2>/dev/null || true` — Резервные копии
28. `sha256sum ~/ico2027/10_WHEELS/* | tail` — Резервные копии
28. `find ~/ico2027/13_SOLUTIONS_PRIVATE -type f -ls` — Резервные копии
28. `find ~/ico2027/14_INCOMING -type f -ls` — Резервные копии
28. `find ~/ico2027/15_OUTPUT -type f -ls` — Резервные копии
28. `date -Is > ~/ico2027/99_BACKUP/backup-date.txt` — Резервные копии
28. `find ~/ico2027 -type f -printf "%s %p\n" | sort -n | tail -20` — Резервные копии

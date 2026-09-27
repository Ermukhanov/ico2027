# Локальный мини-CTF ICO prep

12 полностью офлайн-заданий: 2 Reverse, 2 Pwn, 2 Web, 2 Crypto, 2 Forensics, 1 Stego и 1 Networking. Все артефакты хранятся здесь; веб-стенд привязывается только к `127.0.0.1`. Pwn ELF предназначены для Linux x86-64, исходники приложены.

## Маршрут

1. Прочитай условие и посчитай хеш артефакта.
2. Запиши гипотезу и проверь её подходящей локальной командой.
3. Запусти `solve/solve.py` только после самостоятельной попытки.
4. Сверь шаги с `writeup.md`; останови локальный сервер после Web-задачи.

## Задания

- [Кодирование Base64](challenges/crypto-01-base64/README.md) — `crypto-01-base64`.
- [Однобайтовый XOR](challenges/crypto-02-single-xor/README.md) — `crypto-02-single-xor`.
- [Временная линия веб-журнала](challenges/forensics-01-web-log/README.md) — `forensics-01-web-log`.
- [Комментарий ZIP как улика](challenges/forensics-02-archive-metadata/README.md) — `forensics-02-archive-metadata`.
- [Фрагменты в DNS-запросах](challenges/network-01-dns-pcap/README.md) — `network-01-dns-pcap`.
- [ret2win в локальном бинарнике](challenges/pwn-01-ret2win/README.md) — `pwn-01-ret2win`.
- [Усечение длины до uint8_t](challenges/pwn-02-integer-wrap/README.md) — `pwn-02-integer-wrap`.
- [Скрытая строка в checker](challenges/reverse-01-xor-checker/README.md) — `reverse-01-xor-checker`.
- [Обратное преобразование](challenges/reverse-02-inverse-transform/README.md) — `reverse-02-inverse-transform`.
- [Младший бит пикселя](challenges/stego-01-pgm-lsb/README.md) — `stego-01-pgm-lsb`.
- [Просмотр исходника страницы](challenges/web-01-source-review/README.md) — `web-01-source-review`.
- [Локальный просмотрщик документов](challenges/web-02-local-path/README.md) — `web-02-local-path`.

Все флаги учебные; внешние сервисы не затрагиваются.

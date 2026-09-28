#!/usr/bin/env bash
# auto_triage.sh — эвристический (без ИИ) определитель категории задачи по файлу.
# Использование: ./auto_triage.sh path/to/file
set -uo pipefail
F="${1:?usage: auto_triage.sh FILE}"
[ -f "$F" ] || { echo "Файл не найден: $F"; exit 1; }

echo "==================== БАЗОВАЯ ИНФОРМАЦИЯ ===================="
TYPE=$(file -b "$F")
SIZE=$(stat -c%s "$F" 2>/dev/null || stat -f%z "$F")
SHA=$(sha256sum "$F" 2>/dev/null | awk '{print $1}')
echo "Файл:   $F"
echo "Тип:    $TYPE"
echo "Размер: $SIZE байт"
echo "SHA256: $SHA"
echo

HEX=$(xxd -l 8 -p "$F" 2>/dev/null)
echo "Первые 8 байт (hex): $HEX"
echo

# --- Эвристики по типу/сигнатуре ---
CATS=()

case "$TYPE" in
  *"ELF"*)
    CATS+=("REVERSE/PWN")
    echo "-> ELF-бинарник. Похоже на REVERSE или PWN."
    echo "   Команды:"
    echo "     checksec --file=\"$F\""
    echo "     readelf -h \"$F\"; readelf -S \"$F\"; readelf -s \"$F\""
    echo "     objdump -d -M intel \"$F\" | less"
    echo "     strings -a \"$F\" | grep -Ei 'flag|secret|admin|win|password|token'"
    echo "   Если есть удалённый сервис (nc host port) -> склоняется к PWN."
    echo "   Если только сам бинарник без сети -> склоняется к REVERSE."
    ;;
  *"PE32"*|*"MS-DOS"*)
    CATS+=("REVERSE")
    echo "-> Windows PE-бинарник. REVERSE."
    echo "   Команды: python3 ~/ico2027/scripts/pe_triage.py \"$F\""
    ;;
  *"PNG image"*)
    CATS+=("STEGO/FORENSICS")
    echo "-> PNG. STEGO или FORENSICS."
    echo "   Команды:"
    echo "     zsteg \"$F\""
    echo "     python3 ~/ico2027/scripts/lsb_image.py \"$F\""
    echo "     python3 ~/ico2027/scripts/png_chunks.py \"$F\"   # проверка CRC чанков"
    echo "     exiftool \"$F\""
    ;;
  *"JPEG image"*|*"GIF image"*|*"bitmap"*)
    CATS+=("STEGO/FORENSICS")
    echo "-> Изображение. STEGO/FORENSICS."
    echo "   Команды: exiftool \"$F\"; binwalk \"$F\"; zsteg \"$F\" (для BMP/PNG)"
    ;;
  *"tcpdump capture"*|*"pcap"*)
    CATS+=("NETWORK/FORENSICS")
    echo "-> PCAP. NETWORK/FORENSICS."
    echo "   Команды:"
    echo "     capinfos \"$F\""
    echo "     tshark -r \"$F\" -q -z io,phs"
    echo "     tshark -r \"$F\" -Y dns -T fields -e dns.qry.name | sort -u"
    echo "     tshark -r \"$F\" -Y 'http.request'"
    ;;
  *"Zip archive"*)
    CATS+=("FORENSICS/CRYPTO")
    echo "-> ZIP-архив. FORENSICS (может быть с паролем -> CRYPTO)."
    echo "   Команды:"
    echo "     unzip -l \"$F\""
    echo "     zip2john \"$F\" > hash.txt && john hash.txt   # если запаролен"
    echo "     binwalk \"$F\""
    ;;
  *"ASCII text"*|*"Unicode text"*|*"UTF-8"*)
    CATS+=("CRYPTO/WEB")
    echo "-> Текстовый файл. CRYPTO (закодированная строка) или WEB (лог/HTML/JSON)."
    echo "   Команды:"
    echo "     python3 ~/ico2027/scripts/base_decode.py \"$F\""
    echo "     python3 ~/ico2027/scripts/xor_singlebyte.py \"$F\""
    echo "     head -50 \"$F\"   # посмотреть глазами формат"
    ;;
  *"RIFF"*"WAVE"*|*"Audio"*)
    CATS+=("STEGO")
    echo "-> Аудио. STEGO."
    echo "   Команды: sox \"$F\" -n spectrogram -o spec.png; ffprobe -hide_banner \"$F\""
    ;;
  *)
    echo "-> Тип не распознан однозначно эвристикой. Проверь вручную:"
    echo "   strings -a -n 6 \"$F\" | head -50"
    echo "   binwalk \"$F\""
    ;;
esac

echo
echo "==================== ЭНТРОПИЯ ===================="
if command -v python3 >/dev/null; then
  ENT=$(python3 ~/ico2027/scripts/entropy.py "$F" 2>/dev/null || echo "n/a")
  echo "Энтропия: $ENT (близко к 8.0 = зашифровано/сжато -> смотри CRYPTO; низкая = читаемый формат)"
fi

echo
echo "==================== ПОДОЗРИТЕЛЬНЫЕ СТРОКИ ===================="
strings -a -n 6 "$F" 2>/dev/null | grep -Ei 'flag|ico\{|key|pass|token|secret|http|admin' | head -20

echo
echo "==================== РЕКОМЕНДАЦИЯ ===================="
echo "Похожие категории: ${CATS[*]:-неясно, проверь вручную}"
echo "Дальше открой ONE_PAGE.md -> раздел по категории выше."

#!/usr/bin/env bash
# machine.sh — единая точка входа. Один файл -> полный авторазбор.
# Умеет: определять тип, лезть внутрь zip/tar рекурсивно,
# находить подозрительные строки и САМА пробовать их раскодировать
# (base64 / hex / rot13), без ИИ — чистые эвристики + python.
#
# Использование: ./machine.sh path/to/file
set -uo pipefail
DEPTH="${2:-0}"
INDENT=$(printf '%*s' "$((DEPTH*2))" '')
F="${1:?usage: machine.sh FILE}"
[ -f "$F" ] || { echo "${INDENT}Файл не найден: $F"; exit 1; }

echo "${INDENT}================ $F ================"
TYPE=$(file -b "$F")
SIZE=$(stat -c%s "$F" 2>/dev/null || stat -f%z "$F")
echo "${INDENT}Тип: $TYPE | Размер: $SIZE байт"
echo "${INDENT}SHA256: $(sha256sum "$F" 2>/dev/null | awk '{print $1}')"

# ---------- Рекурсия в архивы ----------
case "$TYPE" in
  *"Zip archive"*)
    echo "${INDENT}-> ZIP-архив. Распаковываю и захожу внутрь рекурсивно..."
    TMPD=$(mktemp -d)
    if unzip -P "" -o "$F" -d "$TMPD" >/dev/null 2>&1; then
      find "$TMPD" -type f | while read -r inner; do
        bash "$0" "$inner" "$((DEPTH+1))"
      done
    else
      echo "${INDENT}   Архив запаролен. Попробуй: zip2john \"$F\" > hash.txt && john hash.txt"
    fi
    exit 0
    ;;
  *"gzip compressed"*|*"tar archive"*)
    echo "${INDENT}-> TAR/GZIP-архив. Распаковываю рекурсивно..."
    TMPD=$(mktemp -d)
    tar -xzf "$F" -C "$TMPD" 2>/dev/null || tar -xf "$F" -C "$TMPD" 2>/dev/null
    find "$TMPD" -type f | while read -r inner; do
      bash "$0" "$inner" "$((DEPTH+1))"
    done
    exit 0
    ;;
esac

# ---------- Категория по типу (как раньше) ----------
CATS=()
case "$TYPE" in
  *"ELF"*)              CATS+=("REVERSE/PWN") ;;
  *"PE32"*|*"MS-DOS"*)  CATS+=("REVERSE") ;;
  *"PNG image"*)        CATS+=("STEGO/FORENSICS") ;;
  *"JPEG"*|*"GIF"*|*"bitmap"*) CATS+=("STEGO/FORENSICS") ;;
  *"tcpdump capture"*|*"pcap"*) CATS+=("NETWORK/FORENSICS") ;;
  *"ASCII text"*|*"UTF-8"*|*"Unicode text"*) CATS+=("CRYPTO/WEB") ;;
  *"RIFF"*|*"Audio"*)   CATS+=("STEGO") ;;
  *) CATS+=("неясно") ;;
esac
echo "${INDENT}Категория: ${CATS[*]}"

# ---------- Энтропия ----------
if command -v python3 >/dev/null 2>&1 && [ -f ~/ico2027/scripts/entropy.py ]; then
  ENT=$(python3 ~/ico2027/scripts/entropy.py "$F" 2>/dev/null)
  echo "${INDENT}Энтропия: ${ENT:-n/a}"
fi

# ---------- Найти подозрительные строки И САМОМУ их раскодировать ----------
echo "${INDENT}-- Подозрительные строки + попытка авто-декода --"
strings -a -n 8 "$F" 2>/dev/null | grep -Ei 'flag|ico\{|key|pass|token|secret|http|[A-Za-z0-9+/]{20,}={0,2}' | sort -u | head -15 | while read -r line; do
  echo "${INDENT}  RAW: $line"

  # Попытка base64
  DECODED_B64=$(echo "$line" | grep -oE '[A-Za-z0-9+/]{16,}={0,2}' | while read -r chunk; do
    echo "$chunk" | base64 -d 2>/dev/null | strings -a
  done)
  [ -n "$DECODED_B64" ] && echo "${INDENT}    -> base64:  $DECODED_B64"

  # Попытка hex
  if echo "$line" | grep -qE '^[0-9a-fA-F]{16,}$'; then
    DECODED_HEX=$(echo "$line" | xxd -r -p 2>/dev/null | strings -a)
    [ -n "$DECODED_HEX" ] && echo "${INDENT}    -> hex:     $DECODED_HEX"
  fi

  # Попытка rot13
  DECODED_ROT=$(echo "$line" | tr 'A-Za-z' 'N-ZA-Mn-za-m')
  [ "$DECODED_ROT" != "$line" ] && echo "${INDENT}    -> rot13:   $DECODED_ROT"
done

echo "${INDENT}-- Рекомендация: MAIN_CHEATSHEET.md, раздел ${CATS[*]} --"
echo

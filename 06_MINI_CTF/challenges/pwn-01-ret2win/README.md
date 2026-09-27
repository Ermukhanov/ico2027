# ret2win в локальном бинарнике

**Категория:** Pwn. **Цель:** найти путь управления в `win`, оценить смещение и вызвать функцию победы.

`challenge/chall` — заранее собранный x86-64 ELF; рядом лежит исходник. Пересобирай только локально командой `gcc -O0 -fno-stack-protector -fno-omit-frame-pointer -no-pie -Wno-implicit-function-declaration -Wno-deprecated-declarations -o challenge/chall challenge/chall.c`.

Начни с `file`, `checksec`, `nm -n` и `gdb`. Ввод идёт только через stdin запущенного локального процесса. Решатель: `python3 solve/solve.py` из этого каталога. Это намеренно уязвимый учебный ELF, не запускай его как сетевой сервис.

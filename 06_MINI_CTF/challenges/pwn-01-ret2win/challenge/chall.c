#include <stdio.h>
#include <unistd.h>
void win(void) { puts("ICO{ret2win_local}"); }
__attribute__((noinline)) void vuln(void) { char buf[40]; puts("input:"); gets(buf); }
int main(void) { setvbuf(stdout, NULL, _IONBF, 0); vuln(); puts("returned safely"); return 0; }

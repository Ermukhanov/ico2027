#include <stdint.h>
#include <stdio.h>
int main(void) { unsigned int requested = 0; printf("requested bytes: "); if (scanf("%u", &requested) != 1) return 1; uint8_t stored = (uint8_t)requested; if (requested > 255 && stored == 0) puts("ICO{integer_wrap}"); else puts("denied"); return 0; }

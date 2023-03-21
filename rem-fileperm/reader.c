#include <stdio.h>

int main() {
    FILE *fp;
    char ch;

    fp = fopen("flag.txt", "r");
    if (fp == NULL) {
        printf("Failed to open file\n");
        return 1;
    }

    while ((ch = fgetc(fp)) != EOF) {
        putchar(ch);
    }

    fclose(fp);
    return 0;
}

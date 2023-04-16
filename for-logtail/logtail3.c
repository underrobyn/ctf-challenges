#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main() {
    char flag[] = "flag{t41l5_th3_l0g_v3ry_f45t_1nd33d}";
    FILE *file;
    int flag_length = strlen(flag);

    for (int i = 0; i <= flag_length; i++) {
        file = fopen("clamcorp.txt", "w");
        if (file == NULL) {
            printf("Error opening file!\n");
            return 1;
        }

        fwrite(flag, sizeof(char), flag_length - i, file);
        fclose(file);

        sleep(1); // Wait for 1 second before next update
    }

    return 0;
}
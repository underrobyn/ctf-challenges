#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define FILENAME ".clamcorp.out"
#define ENCODING_KEY 0x12

void encode_flag(char *flag) {
    for (int i = 0; i < strlen(flag); i++) {
        flag[i] ^= ENCODING_KEY;
    }
}

void overwrite_file(FILE *file) {
    char rand_string[36];
    while (1) {
        int wait_time = rand() % 301 + 200;
        usleep(wait_time * 1000);
        printf(":(\n");

        // generate a random string of length 16
        for (int i = 0; i < 36; i++) {
            rand_string[i] = 'A' + rand() % 104;
        }
        rand_string[36] = '\0\n';

        fseek(file, 0, SEEK_SET);
        fwrite(rand_string, sizeof(char), strlen(rand_string), file);
        fflush(file);
    }
}

int main() {
    // seed the random number generator with the current time
    srand(time(NULL));

    // open the file for writing
    FILE *file = fopen(FILENAME, "w");
    if (!file) {
        printf("Failed to open file\n");
        return 1;
    }

    // encode the flag and write it to the file
    // char encoded_flag[] = "flag{t41l5_th3_l0g_v3ry_f45t_1nd33d}";  // encoded flag

    // printf("%s\n", encoded_flag);
    // printf("%s\n", encoded_flag2);
    // encode_flag(encoded_flag);
    // printf("%s\n", encoded_flag);
    // printf("%s\n", encoded_flag2);
    char encoded_flag2[] = "t~suif&#~'Mfz!M~\"uMd!`kMt&'fM#|v!!vo";  // encoded flag
    encode_flag(encoded_flag2);
    fwrite(encoded_flag2, sizeof(char), strlen(encoded_flag2), file);
    fflush(file);
    printf(":)\n");

    // overwrite the file with random data until the program is terminated or the file is closed
    overwrite_file(file);

    // close the file
    fclose(file);

    return 0;
}

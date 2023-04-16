#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define FILENAME ".clamcorp"
#define ENCODING_KEY 0x12

void encode_flag(char *flag) {
    for (int i = 0; i < strlen(flag); i++) {
        flag[i] ^= ENCODING_KEY;
    }
}

void overwrite_file() {
    char rand_string[38];
    while (1) {
        FILE *file = fopen(FILENAME, "w");
        if (!file) {
            printf("Failed to open file\n");
            continue;
        }

        // generate a random string of length 16
        for (int i = 0; i < 36; i++) {
            rand_string[i] = 'A' + rand() % 104;
        }
        rand_string[36] = '\0';
        rand_string[37] = '\n';

        fseek(file, 0, SEEK_SET);
        fwrite(rand_string, sizeof(char), strlen(rand_string), file);
        fflush(file);

        int wait_time = rand() % 301 + 200;
        usleep(wait_time * 1000);

        fclose(file);
        printf(":(");
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
    char encoded_flag[] = "t~suif&#~'Mfz!M~\"uMd!`kMt&'fM#|v!!vo";
    encode_flag(encoded_flag);
    fwrite(encoded_flag, sizeof(char), strlen(encoded_flag), file);
    fflush(file);
    printf(":)");

    // close the file
    fclose(file);

    // overwrite the file with random data until the program is terminated or the file is closed
    overwrite_file();

    return 0;
}

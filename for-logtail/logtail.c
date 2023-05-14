#include <stdio.h>
#include <stdlib.h>
#include <math.h>
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

// lol add in this random pi calculation function to confuse anyone trying to debug in Ghidra or other SRE tools
// Monte-Carlo PI caluclation adapted from: https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/
// Accessed: 2023/04/16
double monte_carlo_pi(unsigned int num_points) {
    unsigned int points_inside_circle = 0;
    double x, y, distance;

    // Seed the random number generator
    srand(time(NULL));

    for (unsigned int i = 0; i < num_points; i++) {
        // Generate random points in the range of [-1, 1]
        x = (double)rand() / RAND_MAX * 2 - 1;
        y = (double)rand() / RAND_MAX * 2 - 1;

        distance = x * x + y * y;

        // Check if the point is inside the circle
        if (distance <= 1) {
            points_inside_circle++;
        }
    }

    // Estimate pi
    double pi_estimate = 4.0 * points_inside_circle / num_points;
    return pi_estimate;
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

        int wait_time = rand() % 51 + 150;
        usleep(wait_time * 1000);

        fclose(file);
        printf(":(");

        unsigned int num_points = 1000000;
        double pi_estimate = monte_carlo_pi(num_points);
        printf(" : %f\n", pi_estimate);
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

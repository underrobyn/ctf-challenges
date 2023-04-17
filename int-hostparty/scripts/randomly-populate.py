import os
import random
import string


def random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def random_file_name():
    return random_string(10) + '.tmp'


def generate_random_files(num_files, file_size):
    for _ in range(num_files):
        file_name = random_file_name()
        with open(f'/srv/ftp/tmp/{file_name}', 'w') as f:
            for _ in range(file_size):
                f.write(random_string(1024))
                f.write('\n')


num_files = 10  # Set the number of files you want to generate
file_size = 50  # Set the file size in KB

generate_random_files(num_files, file_size)

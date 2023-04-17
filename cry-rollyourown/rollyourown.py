#!/bin/python3

def xor_cipher(text: str, key) -> str:
    result = []
    key = format(key, '016b')

    for char in text:
        char_bin = format(ord(char), '08b')
        encrypted_char = int(char_bin, 2) ^ int(key, 2)
        result.append(chr(encrypted_char))

    return ''.join(result)


def encrypt(text, key):
    return xor_cipher(text, key)


def decrypt(encrypted_text, key):
    return xor_cipher(encrypted_text, key)


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == "__main__":
    key = 0

    encrypted_file_path = 'encrypted.txt'
    decrypted_file_path = 'decrypted2.txt'

    encrypted_text = read_file(encrypted_file_path)

    decrypted_text = decrypt(encrypted_text, key)
    write_file(decrypted_file_path, decrypted_text)
    print('Decrypted text saved to:', decrypted_file_path)

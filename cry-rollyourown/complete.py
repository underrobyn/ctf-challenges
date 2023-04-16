#!/bin/python3

def xor_cipher(text, key):
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

if __name__ == "__main__":
    key = 42069  # A 10-bit key (range from 0 to 65535)
    text = "flag{d0nt_r011_y0ur_0wn_crypt0}"

    input_file_path = "input.txt"
    encrypted_file_path = "encrypted.txt"
    decrypted_file_path = "decrypted.txt"

    text = read_file(input_file_path)

    encrypted_text = encrypt(text, key)
    write_file(encrypted_file_path, encrypted_text)
    print("Encrypted text saved to:", encrypted_file_path)

    decrypted_text = decrypt(encrypted_text, key)
    write_file(decrypted_file_path, decrypted_text)
    print("Decrypted text saved to:", decrypted_file_path)

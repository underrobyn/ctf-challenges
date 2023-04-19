import socket
import random
import string


def random_string(n: int) -> str:
    chars = string.ascii_letters + string.digits + '{}'
    return ''.join(random.choice(chars) for _ in range(n))


def main() -> None:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1717))

    chunk_size = 4
    n = 32 * chunk_size

    flag = "flag{41w4y5_1n5p3ct_ur_p4ck3t5}"
    data = f"{random_string(n)}{flag}{random_string(n)}"
    print(data)

    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        client_socket.send(chunk.encode())

    client_socket.close()


if __name__ == '__main__':
    main()

import socket


def main() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 1717))
    server_socket.listen(1)

    print("Server listening on port 1717")
    connection, address = server_socket.accept()
    print(f"Connection from {address}")

    data = ''
    chunk_size = 4  # You can change this value to modify the packet size

    while True:
        chunk = connection.recv(chunk_size).decode()
        print(chunk)
        if not chunk:
            break
        data += chunk

    print("Received data:", data)
    connection.close()
    server_socket.close()


if __name__ == '__main__':
    while True:
        main()

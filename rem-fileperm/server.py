import logging

import nclib
from os import system


class NetCatServer:

    _server: nclib.TCPServer

    def __init__(self, host: str = '0.0.0.0', port: int = 9000):
        self.client_commands = []

        self.host = host
        self.port = port

        self._setup()

    def _setup(self) -> None:
        self._server = nclib.TCPServer((self.host, self.port))

    def _run_command(self, client):
        return system(self.client_commands[client.peer][-1])

    def listen(self):
        logging.info(f'Listening on {self.port}')
        for client in self._server:
            self._handle_client(client)

    def _handle_client(self, client):
        logging.info('Connected to %s:%d' % client.peer)
        self.client_commands[client.peer] = []

        command = ""
        while command != "exit":
            try:
                if len(command) > 0:
                    if command in client.readln().decode('utf-8').strip(" "):
                        continue

                # get output until dollar sign (bash --posix forces bash-X.X$)
                data = client.read_until('$')
                print(data.decode('utf-8'), end="")

                # get user input command and write command to socket
                command = input(" ")
                client.writeln(command)
                print(command)
            except Exception as e:
                print("\nException Occurred\n")
                print(e)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(asctime)s - %(message)s')
    ncs = NetCatServer('127.0.0.1', 9000)
    ncs.listen()

import socket

def ascii_art():
    print('''
    ⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⣀⣴⣦⡀⠀⠀⠀⢶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀                 *                                                   *
    ⠀⠀⠀⠀⢠⣾⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⣦⠀⠀⢾⣿⣿⣿⣷⡀⠀⠀⢸⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀        *   ✧  "I helped Lain  ✧  this is going to  ✧       *
    ⠀⠀⠀⢀⣿⠃⠀⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⢻⣧⠀⠀⠙⢿⣿⣿⣧⠀⠀⠀⣿⣿⣿⠇⠀⣶⣄⠀⠀⠀        *                                                   *
    ⠀⠀⠀⢸⣿⠀⠀⠀⠑⠄⠀⠀⠀⠀⠀⠀⠀⠔⠁⠀⠀⢸⣿⠀⠀⠀⠀⠻⣿⣿⡆⠀⠀⣿⣿⣿⠀⢸⣿⣿⣦⠀⠀        *      ✧  make me a hero  ✧  with the  ✧            *
    ⠀⠀⠀⠀⠛⢁⠔⠒⣶⠲⣄⠀⠀⠀⠀⢀⡴⢲⡖⠒⢄⠘⠋⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⣿⣿⡏⢠⣿⣿⣿⠃⠀⠀        *                                                   *
    ⠀⠀⠀⠀⠀⡁⠀⢸⣿⡇⠈⢣⠀⠀⠀⠊⠀⣿⣿⠀⠀⡑⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⣿⡟⢀⣾⣿⡟⠁⢀⣶⡀        *             ✧  local users"  ✧                    *
    ⠀⠀⠀⢀⡀⠈⠂⠄⠻⠡⠐⠈⣀⢀⣀⠐⠠⠹⠏⠀⠊⠀⣀⠄⠀⠀⠀⠀⠀⠸⠀⠀⢰⠟⢀⣾⡿⠋⢀⣴⣿⣿⡇
    ⠀⠀⠀⠘⡅⡇⣆⣄⣀⡀⠀⠀⠉⠛⠁⠀⠀⣀⡀⡄⠆⡳⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⠟⠉⢀⣴⣿⡿⠟⢉⡄
    ⠀⠀⠀⠀⠀⠃⠿⣿⣟⣞⣿⡾⣟⣟⣿⣾⡟⣾⣿⡟⠇⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠖⠛⠉⢁⣤⣶⣿⠁
    ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠚⠛⠻⠿⠛⠛⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢴⣾⣿⣿⣿⡏⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⢶⣾⣿⣿⣿⡆⠀⠀⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣄⠀⠀⠀⠀⠈⢿⣿⣿⣿⡇⠀⠀⢹⣿⣿⣿⡇⠀⠀⣤⣀⣀⡀⢤⣤⣶⣾⡿⠋⠀⠀⠀
    ⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠙⠛⠻⠧⠀⠀⣿⣿⣿⣷⡀⠙⠿⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⢠⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣼⣿⣿⣿⣶⣤⣤⣤⣴⣶⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠹⣿⣿⣿⣿⣿⣿⠿⠟⠛⠁⢀⣼⣿⣶⣶⣶⣶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠈⠉⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠐⠚⠿⠿⠿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')


def start_chershire(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f'[*]Now listening on {host}:{port}')

    while True:
        client_socket, addr = server.accept()
        print(f'[*]{addr} connected')
        handle_client(client_socket)


def handle_client(client_socket):
    while True:
        try:
            command = input('Command> ')

            if command.lower() == 'exit':
                client_socket.send(b'exit')
                client_socket.close()
                break
            client_socket.send(command.encode())

            response = client_socket.recv(4096).decode()
            print(response, end="")
        except Exception as e:
            print(f'Error: {e}')
            client_socket.close()
            break


if __name__ == "__main__":
    ascii_art()
    start_chershire('127.0.0.1', 9999)

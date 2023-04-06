import lancelot

def handle_client(client_sock):
    try:
        while True:
            question = lancelot.recv_until(client_sock, '?')
            answer = lancelot.qadict[question]
            client_sock.sendall(answer)
    except EOFError:
        client_sock.close()

def server_loop(listen_sock):
    while True:
        client_sock, sockname = listen_sock.accept()
        handle_client(client_sock)

if __name__ == '__main__':
    listen_sock = lancelot.setup()
    server_loop(listen_sock)
active_socks = []
socks2addr = {}


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server_sock.bind(ADDR)
server_sock.listen(10)
active_socks.append(server_sock)

mailbox = queue.Queue()
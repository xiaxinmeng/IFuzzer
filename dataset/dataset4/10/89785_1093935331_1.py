import socket
import ssl
import threading

hostname = '192.168.135.9'
port = 1004

def make_connection():
	context = ssl.SSLContext(ssl.PROTOCOL_TLS)

	with socket.create_connection((hostname, port)) as sock:
		sock.settimeout(300) # use non-blocking I/O
		with context.wrap_socket(sock, server_hostname=hostname) as ssock:
			print(ssock.version())


t=threading.Thread(target=make_connection)
t.start()
t.join()

# Script implements ghost client (that does not send anything to server but keeps connection active until server socket timeouts or forever if socket timeouts are not working)
# Usage - after https.py server is launched run using: python3 ghost.py
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 443))
print("connected")

while True:
	print("ghosting started")
	data = sock.recv(4096) # read to block
	if not data:
		break
	print(data)
	
print("done.")

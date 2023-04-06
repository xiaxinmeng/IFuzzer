
import socket
old_accept = socket.socket.accept
def patch_accept(self):
	newsock, addr = old_accept(self)
	newsock.settimeout(2) # sets the client socket timeout
	print("socket.accept patched")
	return newsock, addr

socket.socket.accept = patch_accept

# TODO: now run all the SSL server socket code here

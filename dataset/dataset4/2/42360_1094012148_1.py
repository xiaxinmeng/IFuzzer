bytecount = socket.send(Request)
while  XML[-10:-1] != EOM: 
	XML += socket.recv(length)

socket.close()
for i in range(2):
	client.sendto(data, (sys.argv[1], 123))
	data, address = client.recvfrom(1024)
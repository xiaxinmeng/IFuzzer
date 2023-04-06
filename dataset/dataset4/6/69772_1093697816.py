def x(data, sock):
    while True:
        # some code here    
        try:
            sock.sendall(data)
            return
        except timeout:
            pass
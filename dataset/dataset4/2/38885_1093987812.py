def max_server_sockets():
    sl = []
    while 1:
        try:
            s = socket.socket (socket.AF_INET, 
socket.SOCK_STREAM)
            s.bind (('',0))
            s.listen(5)
            sl.append (s)
        except:
            break
    num = len(sl)
    for s in sl:
        s.close()
    del sl
    return num
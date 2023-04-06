data = s.recv(1024).decode('utf-8')
q, w, e = struct.unpack('!IHQ', s.recv(4))
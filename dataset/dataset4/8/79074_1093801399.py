s.send(struct.pack('!I', x))
q, w, e = struct.unpack('!IHQ', s.recv(4))
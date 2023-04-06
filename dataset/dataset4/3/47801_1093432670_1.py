p = Process(target=_echo, args=(child_conn,))
p.daemon = True
p.start()

really_big_msg = latin('X') * (1024 * 1024 * 32)
conn.send_bytes(really_big_msg)
assert conn.recv_bytes() == really_big_msg

conn.send_bytes(SENTINEL)                          # tell child to quit
child_conn.close()
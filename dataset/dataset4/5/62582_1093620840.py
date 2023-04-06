from multiprocessing import Pipe
a, b = Pipe()
b.send_bytes(b'')
a.poll() and a.poll()
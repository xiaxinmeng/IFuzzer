import numpy as np
from multiprocessing import Pipe
p1, p2 = Pipe()
arr = np.zeros((3, 5, 6), dtype=np.uint8)
p2.send_bytes(arr)
pm = p1.recv_bytes()
print(pm)
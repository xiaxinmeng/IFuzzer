from threading import Thread
import pdb
n_threads = 8

def f(self):
    self.obj[0] = 0
    t = 0
    while True:
        if t != self.obj[0]:
            pdb.set_trace() # should not happen
        t += 1
        self.obj[0] += 1

for _ in range(n_threads):
    t = Thread(target=lambda: f(t))
    t.obj = [0]
    t.start()
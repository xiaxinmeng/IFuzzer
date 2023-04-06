import os
import time
from multiprocessing import Process

p = Process(target=lambda:os.execlp('bash', 'bash', '-c', 'sleep 1.5'))
t0 = time.time()
p.start()
p.join(0.1)
print(time.time() - t0)
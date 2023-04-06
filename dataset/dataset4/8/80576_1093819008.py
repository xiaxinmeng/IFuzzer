from concurrent import futures
import time

complete = False

def complete_eventually():
  global complete
  for _ in range(150000):
    pass
  complete = True

with futures.ThreadPoolExecutor(max_workers=1) as pool:
  pool.submit(complete_eventually)
  print(complete)
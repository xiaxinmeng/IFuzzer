from concurrent import futures
import faulthandler
import sys

def work(iteration, item):
  sys.stdout.write(f'working: iteration={iteration}, item={item}\n')
  sys.stdout.flush()

for i in range(0, 10000):
    faulthandler.dump_traceback_later(20, exit=True)
    with futures.ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(work, i, 1)
        executor.submit(work, i, 2)
    faulthandler.cancel_dump_traceback_later()
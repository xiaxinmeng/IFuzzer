import threading
import thread

_lock = threading.RLock()
def run():
  _lock.acquire()
  _lock.release()

for x in range(0, 100):
  thread.start_new_thread(run, ())
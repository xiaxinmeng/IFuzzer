import time
import threading
 
event = threading.Event()
 
def target():
    event.wait()
    print('thread done')
 
t = threading.Thread(target=target)
t.start()
print('joining now')
try:
    t.join()
except KeyboardInterrupt:
    pass
print(t.is_alive())
event.set()
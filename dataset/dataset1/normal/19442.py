import time
import threading

def open_sleep():
    fileobj = open(__file__, 'rb')
    time.sleep(0.2)

new_thread = threading.Thread(target=open_sleep)
new_thread.daemon = True
new_thread.start()
if 0:
    new_thread.join()
else:
    time.sleep(0.01)


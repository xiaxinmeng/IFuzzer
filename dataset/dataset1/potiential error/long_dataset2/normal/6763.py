import threading
import mimetypes
import time

race_flag = threading.Event()

class Thread(threading.Thread):
    def run(self):
        race_flag.wait()
        mimetypes.guess_type('sss')


threads = []
for i in range(2):
    t = Thread()
    t.start()
    threads.append(t)

time.sleep(0.5)
print("Run Run Run")
race_flag.set()
time.sleep(1)
[t.join() for t in threads]
print("Your interpreter didn't blow up... sorry")


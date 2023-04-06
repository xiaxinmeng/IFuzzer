
import threading
import time


class U(threading.Thread):
    def run(self):
        time.sleep(1)
        if not x.ident:
            x.start()


x = U()
for u in [U() for i in range(10000)]: u.start()

time.sleep(10)

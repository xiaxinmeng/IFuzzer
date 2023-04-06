import os
from threading import Thread

class Crash(Thread):
    def run(self):
        a = os.popen('ls')
        b = a[1].read()

        # uncommenting these lines fixes the problem
        #     but this isn't really documented as far as
        #     we can tell...
        # a[0].close()
        # a[1].close()

for i in range(1000):
    t = Crash()
    t.start()

    while t.isAlive():
         pass

    print(i)

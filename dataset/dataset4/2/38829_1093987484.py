import os
from threading import Thread

class Crash(Thread):
    def run(self):
        a = os.popen4('ls')
        b = a[1].read()
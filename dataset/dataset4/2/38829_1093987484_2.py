import os

class Crash:
    def run(self):
        a = os.popen4('ls')
        b = a[1].read()

for i in range(1000):
    t = Crash()
    t.run()
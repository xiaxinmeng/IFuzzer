import threading
import time

stopevent = threading.Event()

class TestThread(threading.Thread):
    def run(self):
        """ main control loop """
        print ("Thread ", self.ident, " starts")
        count = 0
        while not stopevent.is_set():
            count += 1
            stopevent.wait(1.0)
            print ("loop ", count, "in thread ", self.ident)
        print ("Thread ", self.ident, " ends")

for i in range (2):
    testthread = TestThread()
    testthread.start()
time.sleep (3)
stopevent.set()
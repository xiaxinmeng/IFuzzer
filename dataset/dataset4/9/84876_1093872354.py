import queue
import threading


class MemoryTest(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = queue.Queue()
        self.cv = threading.Condition()

    def put(self, msg):
        self.queue.put(msg)

        with self.cv:
            self.cv.notify()

    def run(self):
        while True:
            while not self.queue.empty():
                self.queue.get()
                self.queue.task_done()

            with self.cv:
                self.cv.wait_for(lambda: not self.queue.empty())
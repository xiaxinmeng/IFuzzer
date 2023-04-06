# How to Reproduce:
import threading
event = threading.Event()
class Test(threading.Thread):
    def __init__(self, ord):
        super().__init__()
        self.ord = ord
    def run(self):
        event.wait()
        print('Hello, world!', self.ord)
threads = tuple(map(Test, range(8)))
tuple(map(lambda thread: thread.start(), threads))
event.set()
tuple(map(lambda thread: thread.join(), threads))
# EOF
import multiprocessing
import Queue

class TestWorker(multiprocessing.Process):

    def __init__(self, inQueue):
        multiprocessing.Process.__init__(self)
        self.inQueue = inQueue

    def run(self):
        while True:
            try:
                task = self.inQueue.get(False)
            except Queue.Empty:
                # I suppose that Queue.Empty exception is about empty queue 
                # and self.inQueue.empty() must be true in this case
                # try to check it using assert
                assert self.inQueue.empty()
                break


def runTest():
    queue = multiprocessing.Queue()
    for _ in xrange(10**5):
        queue.put(1)
    workers = [TestWorker(queue) for _ in xrange(4)]
    map(lambda w: w.start(), workers)
    map(lambda w: w.join(), workers)


if __name__ == "__main__":
    runTest()
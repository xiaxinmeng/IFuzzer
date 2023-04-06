import threading
from queue import Queue
from timeit import default_timer as timer
import urllib.request


q = Queue()  # Queue technique to pass returns among threads while running


def decrement(numbers):  # CPU bound
    while numbers > 0:
        numbers -= 1
        if not q.empty():
            """I added this method because this thread will run most of the time
            because it's mostly cpu bound"""
            print(numbers)
            print(q.get(block=False))
            print(timer() - start)  # It tell after when exactly I/O bound returns value after both the threads started to run


def get_data():  # I/O bound

    with urllib.request.urlopen("https://www.google.com") as dt:
        q.put(dt.read(), block=False)


if __name__ == "__main__":
    start = timer()
    t1 = threading.Thread(target=get_data)
    #t2 = threading.Thread(target=decrement, args=(10000000,)) #For this I/O responds and returns
    t2 = threading.Thread(target=decrement, args=(100000,)) # I/O doesn't responds at all
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(timer() - start)
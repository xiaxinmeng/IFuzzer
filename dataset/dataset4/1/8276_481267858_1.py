
import threading
import _pickle as cPickle

threads = [threading.Thread(target=cPickle.loads, args=(b'cfoo\nfoo\np0\n.',)) for _ in range(10)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]

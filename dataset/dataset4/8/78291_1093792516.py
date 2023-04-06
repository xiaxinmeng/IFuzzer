threads = [threading.Thread(target=cPickle.loads, args=('cfoo\nfoo\np0\n.',)) for _ in range(2)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
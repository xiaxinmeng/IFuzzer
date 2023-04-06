
import multiprocessing as mp

q = mp.Queue(1)


class FailPickle():
    def __reduce__(self):
        raise ValueError()

q.put(FailPickle())
print("Queue is full:", q.full())
q.put(0)
print(f"Got result: {q.get()}")

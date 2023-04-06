
import threading
import itertools

class C:
    def __iter__(self):
        return self
    def __next__(self):
        return 1

def test(i):
    print(list(i))

i1, i2 = itertools.tee(C())
threading.Thread(target=test, args=(i1,)).start()
print(list(i2))

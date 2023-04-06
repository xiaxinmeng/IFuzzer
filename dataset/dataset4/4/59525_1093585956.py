import threading
class C:
    def __del__(self):
        print("DEL")
ITER = iter([C() for x in range(100)])
def f():
    for obj in ITER:
        pass
for x in range(10):
    t = threading.Thread(target=f)
    t.start()
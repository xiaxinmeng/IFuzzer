import threading
class MyLocal(threading.local):
    pass

l = MyLocal()
l.x = 2
l.__dict__   # returns {}
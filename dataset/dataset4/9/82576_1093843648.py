import weakref

obj = None

class MyObj:
    def __iter__(self):
        global obj
        del obj
        return NotImplemented

obj = MyObj()
p = weakref.proxy(obj)
print(5 in p)
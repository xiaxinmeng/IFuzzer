
import weakref


class Model:
    pass


m = Model()
proxy = weakref.proxy(m)
ref = weakref.ref(m)
print(hash(m))
print(hash(ref))
print(hash(proxy))

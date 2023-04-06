
import weakref

refs = []

class A:
    def __init__(self):
        refs.append(weakref.ref(self))
        #raise RuntimeError() <<< enable this line of code and be surprised!

try:
    A()
finally:
    print(refs[0]())

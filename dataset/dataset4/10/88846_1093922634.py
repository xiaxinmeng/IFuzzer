from weakref import WeakKeyDictionary
class C: pass
d = WeakKeyDictionary()
while True:
    c = C()
    d[c] = [c]
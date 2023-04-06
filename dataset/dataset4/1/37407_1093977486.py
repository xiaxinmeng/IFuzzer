class foo:
    def __init__(self):
        self.wref = weakref.WeakValueDictionary()
        self.wref[id(self)] = self

l = [foo() for x in range(int(sys.argv[1]))]

for i in l:
    i.wref.clear()
    del i.wref
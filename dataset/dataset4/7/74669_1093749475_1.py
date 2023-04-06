class CyclicObject:
    def __init__(self, key, register):
        self.key = key
        self.self = self
        self.register = register
        self.register[self.key] = None

    def __del__(self):
        del self.register[self.key]

while True:
    register = { }
    objs = set([CyclicObject(i, register) for i in range(10000)])

    while len(objs) > 0:
        objs.remove(next(iter(objs)))
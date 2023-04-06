#!/usr/bin/python3

class CyclicObject:
    def __init__(self, key, register):
        self.key = key
        self.self = self
        self.register = register
        self.register[self.key] = None

    def __del__(self):
        del self.register[self.key]

for i in range(0,2):
    register = { }
    objs = set([CyclicObject(i, register) for i in range(100)])

    while len(objs) > 0:
        objs.remove(next(iter(objs)))

        try:
            list(register.items())
        except RuntimeError as err:
            print(err)

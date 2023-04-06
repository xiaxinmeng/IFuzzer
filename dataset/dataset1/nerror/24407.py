class X:
    def __hash__(self):
        print("__hash__ ")
        return 0

    def __eq__(self, o):
        global other

        print("__eq__")
        other.clear()
        return 0

l = [(i,0) for i in range(1, 1337)]
other = dict(l)
other[X()] = 0
d = {X(): 0, 1: 1}
d.update(other)

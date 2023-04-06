class X(str):
    def __hash__(self):
        d.clear()
        return 13

d = {}
d[X()] = X()

e = Exception()
e.__setstate__(d)
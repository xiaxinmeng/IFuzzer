import _elementtree as et

class X:
    def __index__(self):
        e[:] = []
        return 1

e = et.Element("elem")
for _ in range(10):
    e.insert(0, et.Element("child"))
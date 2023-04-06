# For the following kinds of "d"
d = cdt.datetime(1, 2, 3)
d = pydt.datetime(1, 2, 3)
class SubC(cdt.datetime): pass
d = SubC(1, 2, 3)
class SubPy(cdt.datetime): pass
d = SubPy(1, 2, 3)
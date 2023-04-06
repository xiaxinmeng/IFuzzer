b = Obj()
b.d
# equivalent to
type(b).__dict__['d'].__get__(b, type(b))
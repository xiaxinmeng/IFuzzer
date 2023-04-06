class s(str):
    def __radd__(s,o): print('in radd, type(o)')
foo = s()
a = [1] + foo
# prints "in radd <class 'list'>"
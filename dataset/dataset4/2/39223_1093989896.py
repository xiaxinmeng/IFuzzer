class C(object):
    def __setitem__(self, name, value):
        print (name, value)

class D(C):
    def __setitem__(self, name, value):
        super(D, self)[name] = value

d = D()
d['foo'] = 'bar'
class Meth(object):
    def __call__(*args, **kwargs):
        print (args, kwargs)

class X(object):
    def some_method(*args, **kwargs):
        print (args, kwargs)

x = X()
x.some_method(1)
X.some_method = Meth()
x.some_method(1)
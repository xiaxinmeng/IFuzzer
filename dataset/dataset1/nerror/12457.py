#! /usr/bin/python

class Outer(object):
    class Inner(object):
        pass
    pass

inner = Outer.Inner()

print('TYPE:', type(inner))
print('IS INSTANCE of "Outer.Inner"?', isinstance(inner, Outer.Inner))
print('IS INSTANCE of "type(inner)"?', isinstance(inner, type(inner)))
print('IS INSTANCE of "Inner"?', isinstance(inner, Inner))

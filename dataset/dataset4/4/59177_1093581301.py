# this runs with python2.7, not with python3.2
class Foo(object):

    class Bar(object):
        pass

    Attr = [Bar()for n in range(10)]

# solved in this way ...
class Foo(object):

    class Bar(object):
        pass

    Attr = []
    for n in range(10): Attr.append(Bar())
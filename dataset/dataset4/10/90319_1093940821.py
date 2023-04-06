class I(int):
    def __init__(*args, **kwargs): pass
    def __new__(*args, **kwargs): pass

d = {'metaclass': I}
class A(1, 2, 3, **d):
    pass
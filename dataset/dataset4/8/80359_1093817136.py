class MyMeta(type):
    def __new__(cls, *args, **kwargs):
        print('__new__', *args, **kwargs)
        super().__new__(cls, *args, **kwargs)
    
    def __init__(self, a):
        print('__init__', *args, **kwargs)
        super().__init__(*args, **kwargs)

class A(metaclass=MyMeta):
    pass
def callable1(self, x, y):
    pass

class SomeClass(object):
    def __init__(self, x, y):
        pass

    def callable2(self, x, y):
        pass

    def __call__(self, x, y):
        pass

callable3 = SomeClass
callable4 = SomeClass(2, 3)

for callable_ in (callable1, SomeClass(1, 2).callable2, callable3, callable4):
    assert callable(callable_)  # the interpreter can tell me this
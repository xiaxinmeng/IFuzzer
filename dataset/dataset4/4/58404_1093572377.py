class A(object):
    def __new__(cls):
        pdb.set_trace()
        return super(A, cls).__new__()
    def __init__(self):
        self.value = "Foo"
    def __str__(self):
        return self.value
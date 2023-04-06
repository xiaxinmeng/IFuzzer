class A(complex):
    def __init__(self, *args, test):
        self.test = test
    def __new__(cls, *args, test):
        return super().__new__(cls, *args)
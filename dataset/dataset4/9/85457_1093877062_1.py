class B(memoryview):
    def __new__(cls, a):
        return super(B, cls).__new__(cls, a)
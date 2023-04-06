class C():
    def __new__(cls):
        self = object.__new__(cls)
        return self
c = C()
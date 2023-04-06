class E(BaseException):
    def __new__(cls, *args, **kwargs):
        return cls
def a(): yield
a().throw(E)

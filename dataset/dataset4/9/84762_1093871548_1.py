class T(tuple):
    def __new__(cls):
        return tuple.__new__(cls, ("",))

t = T()
def f(a: List[t]): ...
# => SyntaxError: Forward reference must be an expression -- got ''
class Example:
    __slots__ = ('a', 'b')
    def __init__(self, a):
        self.a = a

obj = Example(42)
print(obj.b)
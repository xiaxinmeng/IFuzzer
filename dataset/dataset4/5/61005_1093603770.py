class octint(int):
    'int that displays as octal'
    def __str__(self):
        return oct(self)
    __repr__ = __str__

mode = octint(0o644)
print(mode)

class flags4(int):
    'int that displays as 4 binary flags'
    def __str__(self):
        return '|{:04b}|'.format(self)
    __repr__ = __str__

a = flags4(8)
b = flags4(3)
print(a, b, flags4(a|b))

def f(mode=octint(0o666), flags = flags4(0b1011)): pass

print(f.__defaults__)
import inspect
print(inspect.formatargspec(*inspect.getfullargspec(f)))
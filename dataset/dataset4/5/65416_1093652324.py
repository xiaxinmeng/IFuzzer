def outer():
    def inner():
        inner1
from inspect import getsource
print(getsource(outer))
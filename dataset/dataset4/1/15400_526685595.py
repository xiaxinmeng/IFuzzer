
from typing import ForwardRef, get_type_hints

def namespace1():
    a = ForwardRef('A')

    class A: pass
    def fun(x: a): pass

    get_type_hints(fun, globals(), locals())
    return hash(a)

def namespace2():
    a = ForwardRef('A')

    class A: pass
    def fun(x: a): pass

    get_type_hints(fun, globals(), locals())
    return hash(a)

print(namespace1() == namespace2())

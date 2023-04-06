from functools import partial, partialmethod
from unittest.mock import create_autospec
import inspect

def foo(a, b):
    pass

p = partial(foo, 1)
m = create_autospec(p)
m(1, 2, 3) # passes since signature is set as (*args, **kwargs) the signature of functools.partial constructor. This should throw TypeError under autospec


class A:

    def f(self, a, b):
        print(a, b)

    g = partialmethod(f, 1)

m = create_autospec(A)
m().g(1, 2) # passes since signature is set as (self, b) and self is not skipped in _must_skip thus self=1, b=2. This should throw TypeError under autospec since the valid call is m().g(2)
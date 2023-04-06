from functools import wraps
from typing import get_type_hints

def foo(bar: int = None): ...

@wraps(foo)
def foo2(*args, **kwargs): ...

print(get_type_hints(foo))  # {'bar': typing.Optional[int]}
print(get_type_hints(foo2))  # {'bar': <class 'int'>}
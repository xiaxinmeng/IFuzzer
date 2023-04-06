
from typing import no_type_check, get_type_hints

class A:
    x: int = 1

class B:
    y: str = 'a'

print(get_type_hints(A))  # ok: {'x': <class 'int'>}
print(get_type_hints(B))  # ok: {'y': <class 'str'>}

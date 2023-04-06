
from typing import no_type_check, get_type_hints

class A:
    x: int = 1

@no_type_check
class B:
    y: str = 'a'
    delegate = A  # adding this line will make `A` to have `__no_type_check__` as well

print(get_type_hints(A))  # {}, wait, what?
print(get_type_hints(B))  # {}, ok

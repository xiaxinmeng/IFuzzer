
from typing import get_type_hints
class T:
    str: str = 'a'

get_type_hints(T) # Error.

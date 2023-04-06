from typing import *

def f(arg: str = None):
    pass
print(get_type_hints(f))
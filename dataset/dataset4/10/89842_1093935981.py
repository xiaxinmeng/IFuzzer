from typing import Literal

SomeUsefulAlias = Literal[1, "abc"]

def func(arg: Literal[True, "abc"]):
    if arg is not True:
        arg.capitalize()
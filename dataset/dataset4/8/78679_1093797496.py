from typing import NewType, List
from functools import singledispatch

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

MyType = NewType('MyType', List[int])

@fun.register
def _(arg: MyType , verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)
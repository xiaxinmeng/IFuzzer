from functools import singledispatch

@singledispatch
def func(x):
    print("any")

@func.register
def _(x: list[str]):
    print("list[str]")


func(["a", "b"])


import typing
import foo

BarData: typing.TypeAlias = "Data"

def func1(x: foo.FooData, y: BarData):
    pass

class Data:
    pass

print(typing.get_type_hints(func1))  # incorrectly uses bar.Data twice.



import typing
import foo

def func1(x: foo.FooList1):
    pass

def func2(x: foo.FooList2):
    pass

print(typing.get_type_hints(func1))  # {'x': list['Foo']}
print(typing.get_type_hints(func2))  # NameError: name 'Foo' is not defined.


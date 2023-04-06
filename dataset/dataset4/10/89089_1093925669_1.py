
import typing
import foo

def func3(x: foo.FooType):
    pass

print(typing.get_type_hints(func3))  # NameError: name 'Foo' is not defined.


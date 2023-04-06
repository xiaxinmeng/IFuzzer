def func():
    ...

class MyClass:
    method = func

# magic happens here!
bound_method = MyClass().method
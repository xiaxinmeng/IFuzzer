
def func(cls):
    print(cls)

class MyClass:
    method = classmethod(func)

MyClass.method()
MyClass().method()
MyClass.__dict__['method']()

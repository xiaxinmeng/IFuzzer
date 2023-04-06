@staticmethod
def func():
    print("my func")

class MyClass:
    method = func

func() # A: regular function
MyClass.method() # B: class method
MyClass().method() # C: instance method
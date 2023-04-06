func = len

class MyClass:
    method = func

func("abc") # A: regular function
MyClass.method("abc") # B: class method
MyClass().method("abc") # C: instance method
class MyClass:
    method = len  # built-in function

print(MyClass.method("abc"))
print(MyClass().method("abc"))
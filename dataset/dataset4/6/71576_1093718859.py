class A:
    def foo(self, x):
        pass

class B:
    def foo(self, x, y): # different method signature!
        pass

lst = [A(), B()]

for item in lst:
    item.foo(1)  # raises TypeError: foo() missing 1 required positional argument: 'y'"

for item in lst:
    item.foo(1, 2) # raises "TypeError: foo() takes 2 positional arguments but 3 were given"
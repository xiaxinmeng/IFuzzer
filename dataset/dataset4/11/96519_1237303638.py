class A:
    @property
    def foo(s): pass

a = A()

def f():
    a.foo

for _ in range(8):
    f()
# dissassemble f and inspect that LOAD_ATTR_PROPERTY is inside
for _ in range(x):
    f()
    # dissassemble f and inspect that LOAD_ATTR_PROPERTY is still inside in every single iteration, else fail
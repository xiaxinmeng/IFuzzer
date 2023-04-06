import sys

def foo():
    print(1)

def bar():
    print(2)

if input("case: ") == 1:
    sys.exitfunc = foo
else:
    sys.exitfunc = bar
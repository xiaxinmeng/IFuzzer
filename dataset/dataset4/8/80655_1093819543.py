
import sys


def trace(*args):
    print("trace", args)
    return trace

sys.settrace(trace)


def f():
    f()


print(sys.gettrace())
try:
    f()
except Exception as exc:
    print(exc)
print(sys.gettrace())

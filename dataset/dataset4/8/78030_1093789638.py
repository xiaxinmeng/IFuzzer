import sys

def trace(frame, event, arg):
    pass

def f():
    f()
sys.settrace(trace)
print(sys.gettrace())
try:
    f()
except RuntimeError:
    pass
print(sys.gettrace())
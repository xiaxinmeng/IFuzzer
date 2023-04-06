import linecache, sys

def trace(frame, event, arg):
    # The weird globals here is to avoid a NameError on shutdown...
    if frame.f_code.co_filename == globals().get("__file__"):
        lineno = frame.f_lineno
        print("{} {}: {}".format(event[:4], lineno, linecache.getline(__file__, lineno).rstrip()))
    return trace

print(sys.version)
sys.settrace(trace)

def decorator(func):
    return func

def doit():
    @decorator
    @decorator
    @decorator
    def func(x):
        return x + 1

    print(func(1))

doit()
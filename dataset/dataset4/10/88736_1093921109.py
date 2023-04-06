import linecache, sys

def trace(frame, event, arg):
    # The weird globals here is to avoid a NameError on shutdown...
    if frame.f_code.co_filename == globals().get("__file__"):
        lineno = frame.f_lineno
        print("{} {}: {}".format(event[:4], lineno, linecache.getline(__file__, lineno).rstrip()))
    return trace

def foo(x):
    if x:
        try:
            1/(x - 1)
        except ZeroDivisionError:
            pass

    return x

def test_foo():
    for i in range(2):
        foo(i)

print(sys.version)
sys.settrace(trace)
test_foo()
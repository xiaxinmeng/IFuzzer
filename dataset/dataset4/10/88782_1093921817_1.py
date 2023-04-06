import linecache, sys

def trace(frame, event, arg):
    # The weird globals here is to avoid a NameError on shutdown...
    if frame.f_code.co_filename == globals().get("__file__"):
        lineno = frame.f_lineno
        print("{} {}: {}".format(event[:4], lineno, linecache.getline(__file__, lineno).rstrip()))
    return trace

def f(x):
    try:
        1/0
    except ZeroDivisionError as error:
        if x:
            raise
    return 12

print(sys.version)
sys.settrace(trace)

for x in [0, 1]:
    try:
        print(f(x))
    except:
        print("oops")
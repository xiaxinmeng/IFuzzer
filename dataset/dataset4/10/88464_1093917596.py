import linecache, sys

def trace(frame, event, arg):
    # The weird globals here is to avoid a NameError on shutdown...
    if frame.f_code.co_filename == globals().get("__file__"):
        lineno = frame.f_lineno
        print("{} {}: {}".format(event[:4], lineno, linecache.getline(__file__, lineno).rstrip()))
    return trace

def doit():
    for i in range(2):
        with open("test", "w") as f:
            a = 13
            b = 14
            break
    c = 16

print(sys.version)
sys.settrace(trace)
doit()
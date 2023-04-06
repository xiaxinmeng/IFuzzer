import linecache, sys

def trace(frame, event, arg):
    # The weird globals here is to avoid a NameError on shutdown...
    if frame.f_code.co_filename == globals().get("__file__"):
        lineno = frame.f_lineno
        print("{} {}: {}".format(event[:4], lineno, linecache.getline(__file__, lineno).rstrip()))
    return trace

print(sys.version)
sys.settrace(trace)

def func():
    if A:
        if B:
            if C:
                if D:
                    return False
        else:
            return False
    elif E and F:
        return True

A = B = True
C = False

func()
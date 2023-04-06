import linecache, sys

def trace(frame, event, arg):
    # The weird globals here is to avoid a NameError on shutdown...
    if frame.f_code.co_filename == globals().get("__file__"):
        lineno = frame.f_lineno
        print("{} {}: {}".format(event[:4], lineno, linecache.getline(__file__, lineno).rstrip()))
    return trace

def wrong_loop(x):
    if x:
        if x:
            print(4)
    else:
        pass

print(sys.version)
sys.settrace(trace)

wrong_loop(8)
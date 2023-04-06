import sys

def displayhook(o):
    if o is None:
        return
    __builtins__._ = None
    if isinstance(o, (int, float)):
        print(format(o, '_'))
    else:
        print(repr(o))
    __builtins__._ = o

sys.displayhook = displayhook
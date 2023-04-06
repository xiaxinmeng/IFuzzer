
import sys, types

def tr(frame, event, arg):
    print(frame, event, arg)
    return tr

sys.settrace(tr)

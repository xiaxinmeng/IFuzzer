def trace(frame, event, arg):
    print(frame.f_lineno, event)
    return trace

import sys
sys.settrace(trace)
return_from_finally()
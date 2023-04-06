import sys

def trace(frame, event, arg):
    return trace

sys.settrace(trace)
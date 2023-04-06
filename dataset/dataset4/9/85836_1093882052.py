import sys

def f():
    try:
        for i in []: pass
        return 1
    except:
        return 2

def tracer(frame, event, _):
    if event == 'line':
        print("executing line {}".format(frame.f_lineno))
    return tracer

sys.settrace(tracer)
f()
import sys, signal, time

def trace(frame, event, arg):
    if frame.f_code.co_name == 'foo':
        while 1:
            time.sleep(.02)
    return trace

def foo(): pass

def handler(*args):
    1/0

sys.settrace(trace)
signal.signal(signal.SIGALRM, handler)
signal.alarm(1)
try:
    foo()
except ZeroDivisionError:
    pass

print('trace function:', sys.gettrace())
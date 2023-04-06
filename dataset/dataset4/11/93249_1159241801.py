
import sys
import types

def f():
    return sys._getframe()

tb_next = None
frame = f()
lasti = 0
lineno = 2
tb = types.TracebackType(tb_next, frame, lasti, lineno)

e = KeyboardInterrupt()
raise e.with_traceback(tb)

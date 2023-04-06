import ctypes, thread
ctypes.pythonapi.PyThreadState_SetAsyncExc(
    ctypes.c_long(thread.get_ident()),
    ctypes.py_object(ZeroDivisionError))
for i in range(1000): pass
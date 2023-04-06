def f2():
    pass

def wrapper(func, *args, **kw):
    # CALL_FUNCTION_EX: func(**{}) calls PyObject_Call() with kwargs={} which
    # calls _PyFunction_FastCallDict()
    func(*args, **kw)

def f():
    # CALL_FUNCTION: calling wrapper calls fast_function() which calls
    # _PyEval_EvalCodeWithName() which creates an empty dictionary for kw
    wrapper(f2)

f()
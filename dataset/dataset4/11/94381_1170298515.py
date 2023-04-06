
import sys

py_ = {}
exec("""
import sys

def _create_trace_func(trace):
    local_names = {}

    def _trace_func(frame, event, arg):
        trace.append((event, frame.f_lineno - frame.f_code.co_firstlineno))

        lnames = frame.f_code.co_varnames
        if frame.f_code.co_name in local_names:
            assert lnames == local_names[frame.f_code.co_name]
        else:
            local_names[frame.f_code.co_name] = lnames

        # Currently, the locals dict is empty for Cython code, but not for Python code.
        if frame.f_code.co_name.startswith('py_'):
            # Change this when we start providing proper access to locals.
            assert frame.f_locals, frame.f_code.co_name
        else:
            assert not frame.f_locals, frame.f_code.co_name

        return _trace_func
    return _trace_func

""", py_)
_create_trace_func_py = py_["_create_trace_func"]

def run_trace(func, *args):
    """
    >>> def py_add(a,b):
    ...     x = a+b
    ...     return x

    >>> run_trace(max, 1, 2)
    []
    >>> run_trace(py_add, 1, 2)
    [('call', 0), ('line', 1), ('line', 2), ('return', 2)]
    """
    trace = []
    trace_func = _create_trace_func_py(trace)
    sys.settrace(trace_func)
    try:
        func(*args)
    finally:
        sys.settrace(None)
    return trace

def _have_code_flag(func, flag):
    """Return true if the function ``func`` has a code object with
    ``flag`` in its flags."""
    if ismethod(func):
        func = func.__func__
    return isfunction(func) and bool(code.co_flags & flag)
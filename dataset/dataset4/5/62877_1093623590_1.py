def execute_with_context(ctxt, fn, args):
    with ctxt:
        return fn(*args)
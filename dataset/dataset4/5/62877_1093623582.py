def nest(a, b):
    # currently not possible
    return c

def run_with_context(ctxt, callable):
    # abstract executor
    with ctxt:
        return callable()
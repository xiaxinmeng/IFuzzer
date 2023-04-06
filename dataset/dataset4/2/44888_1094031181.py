from functools import partial

def add(a, b):
    return a + b

append_abc = partial(add, partial.skip, "abc")
assert append_abc("xyz") == "xyzabc"
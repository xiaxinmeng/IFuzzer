import weakref
import functools

if 0:
    from test.support import import_fresh_module
    functools = import_fresh_module('functools', blocked=['_functools'])

@functools.lru_cache
def f(x):
    return x

ref_to_f = weakref.ref(f)
print(ref_to_f)
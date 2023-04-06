import inspect
import sys
import types

def make_set():
    return {z*z for z in range(5)}

print(make_set())

# The set comprehension is turned into a code object expecting a single
# argument called ".0" with should be an iterator over range(5).
if sys.version_info < (3,):
    setcomp_code = make_set.func_code.co_consts[1]
else:
    setcomp_code = make_set.__code__.co_consts[1]
setcomp_func = types.FunctionType(setcomp_code, {})

# We can successfully call the function with the argument it expects.
print(setcomp_func(iter(range(5))))

# But inspect can't figure that out, because the ".0" argument also means
# tuple arguments, which this code object doesn't expect.
print(inspect.getcallargs(setcomp_func, iter(range(5))))
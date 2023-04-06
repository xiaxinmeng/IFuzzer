from inspect import signature

print(signature(a.with_arg))  # prints `(x)`
print(signature(a.no_arg))    # prints `()`
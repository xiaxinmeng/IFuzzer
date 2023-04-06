import importlib._bootstrap
func = importlib._bootstrap._handle_fromlist
code = func.__code__

# Assert initially unquickened.
# Use sets to account for byte order.
if set(code._co_code_adaptive[:2]) != set([{resume}, 0]):
    raise AssertionError()  # <=====================================
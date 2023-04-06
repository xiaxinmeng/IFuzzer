if type(x) == int: return False  # Intentionally excluding subclasses.
try:
    y = float(x)
except OverflowError:
    return False
else:
    ... # existing implementation
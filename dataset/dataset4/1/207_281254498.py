try:
    issc = issubclass(cls, type)
except TypeError: # cls is not a class
    issc = False
if issc:
    # treat it as a regular class:
    return _copy_immutable(x)
class DocDescriptor:
    """Helper for builtins.open.__doc__
    """
    def __get__(self, obj, typ=None):
        return (
            "open(file, mode='r', buffering=-1, encoding=None, "
                 "errors=None, newline=None, closefd=True)\n\n" +
            open.__doc__)

class OpenWrapper:
    """Wrapper for builtins.open


    Trick so that open won't become a bound method when stored
    as a class variable (as dbm.dumb does).

    See initstdio() in [Python/pylifecycle.c](https://github.com/python/cpython/blob/main/Python/pylifecycle.c).
    """
    __doc__ = DocDescriptor()

    def __new__(cls, *args, **kwargs):
        return open(*args, **kwargs)
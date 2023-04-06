class Ignore:
    ''' Context manager to ignore particular exceptions'''

    def __init__(self, *ignored_exceptions):
        self.ignored_exceptions = ignored_exceptions

    def __enter__(self):
        return self

    def __exit__(self, exctype, excinst, exctb):
        if exctype is not None:
            try:
                raise
            except self.ignored_exceptions:
                return True
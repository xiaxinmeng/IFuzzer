class Ignore:
    ''' Context manager to ignore particular exceptions'''

    def __init__(self, *ignored_exceptions):
        self.ignored_exceptions = ignored_exceptions

    def __enter__(self):
        return self

    def __exit__(self, exctype, excinst, exctb):
        return exctype in self.ignored_exceptions
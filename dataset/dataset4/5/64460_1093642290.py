class Picky(object):
    """Options container that returns None for all options.
    """
    def __getstate__(self):
        return {}

    def __getnewargs__(self):
        return ()

    def __getattr__(self, attr):
        return None
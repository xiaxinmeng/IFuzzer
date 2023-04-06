class ContextualZipFile(zipfile.ZipFile):
    """
    Supplement ZipFile class to support context manager for Python 2.6
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __new__(cls, *args, **kwargs):
        """
        Construct a ZipFile or ContextualZipFile as appropriate
        """
        if hasattr(zipfile.ZipFile, '__exit__'):
            return zipfile.ZipFile(*args, **kwargs)
        return super(ContextualZipFile, cls).__new__(cls, *args, **kwargs)
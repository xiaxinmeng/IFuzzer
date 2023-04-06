def showsyntaxerror(self, filename=None):
    """... """
    linecache.cache["<SyntaxError>"] = linecache.cache[filename]  # here
    tkconsole = self.tkconsole
    ...
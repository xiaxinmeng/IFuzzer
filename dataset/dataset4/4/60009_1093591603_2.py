class RedirectStdout:
    ''' Create a context manager for redirecting sys.stdout
        to another file.
    '''
    def __init__(self, new_target):
        self.new_target = new_target

    def __enter__(self):
        self.old_target = sys.stdout
        sys.stdout = self.new_target
        return self

    def __exit__(self, exctype, excinst, exctb):
        sys.stdout = self.old_target
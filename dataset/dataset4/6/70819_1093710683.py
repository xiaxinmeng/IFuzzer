class Public:
    def __init__(self, module):
        """
        module should be the globals() dict from the calling module
        """
        self.module = module
        self.module.setdefault('__all__', [])
    def __call__(self, thing, value=None):
        if isinstance(thing, str):
            self.module[thing] = value
        else:
            self.module[thing.__name__] = thing
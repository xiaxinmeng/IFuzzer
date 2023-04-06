class B:
    def __getattr__(self, name):
        return name in dir(self)
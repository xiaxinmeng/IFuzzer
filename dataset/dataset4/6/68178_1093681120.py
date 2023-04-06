class C(object):
    @property
    def __call__(self):
        return lambda: None
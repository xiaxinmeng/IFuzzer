class Base(object):
    def __init__(self, foo=None, *args, **kwargs):
        super(Base, self).__init__(foo, *args, **kwargs)
Base(foo='bar')
Base('bar', 42)
Base('bar', 42, x=7)
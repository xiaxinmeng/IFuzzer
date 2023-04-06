class Base:
    def __init__(self, foo=None, *, y='hi', **kwargs):
        super(Base, self).__init__(**kwargs)
Base(foo='bar')  # Valid, accepted
Base('bar', 42)  # Raises exception
Base('bar', x=7)  # Raises exception
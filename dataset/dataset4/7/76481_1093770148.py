class MappingView(Sized):
    ...
    def __repr__(self):
        return '{0.__class__.__name__}({0._mapping!r})'.format(self)
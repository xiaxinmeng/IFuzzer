def __getattr__(self, attr):
    if attr == '__wrapped__':
        raise AttributeError('__wrapped__')
    if self.name is None:
        return _Call(name=attr, from_kall=False)
    name = '%s.%s' % (self.name, attr)
    return _Call(name=name, parent=self, from_kall=False)
def filter(self, record):
    rv = True
    if self.filters:
        rv = all(getattr(f, 'filter', f)(record) for f in self.filters)
    return rv
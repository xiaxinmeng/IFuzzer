def filter(self, record):
    return all(getattr(f, 'filter', f)(record) for f in self.filters)
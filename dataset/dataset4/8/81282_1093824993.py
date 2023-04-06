def _filter_callable(filter):
    return filter.filter if hasattr(filter, 'filter') else filter

def filter(self, record):
    filters = map(_filter_callable, self.filters)
    return all(f(record) for f in filters)
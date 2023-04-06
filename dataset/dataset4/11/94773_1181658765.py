
def _allow_reckless_class_checks(depth=3):
    return _caller(depth) in {'abc', 'functools', None}

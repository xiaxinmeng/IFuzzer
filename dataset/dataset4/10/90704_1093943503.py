
for method_name in [
        '__setitem__',
        '__delitem__',
        'append',
        'reverse',
        'extend',
        'pop',
        'remove',
        '__iadd__',
        'insert',
        'sort',
    ]:
        locals()[method_name] = _wrap_deprecated_method(method_name)

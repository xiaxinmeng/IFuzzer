def _copy_func_details(func, funcopy):
    # we explicitly don't copy func.__dict__ into this copy as it would
    # expose original attributes that should be mocked
    for attribute in (
        '__name__', '__doc__', '__text_signature__',
        '__module__', '__defaults__', '__kwdefaults__',
    ):
        try:
            setattr(funcopy, attribute, getattr(func, attribute))
        except AttributeError:
            pass
def dumps(obj, *args, **kwargs):
    if args:
        warnings.warn("The positional arguments are deprecated.",
                     DeprecationWarning, stacklevel=2)
    return _dumps(obj, *args, **kwargs)

def _dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kwargs):
    ...
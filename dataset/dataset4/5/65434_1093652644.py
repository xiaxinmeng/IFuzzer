# in importlib.util
def load(spec_or_name, /, **kwargs):  # or "load_from_spec"
    if isinstance(spec_or_name, str):
        name = spec_or_name
        if not kwargs:
            raise TypeError('missing loader')
        spec = spec_from_loader(name, **kwargs)
    else:
        if kwargs:
            raise TypeError('got unexpected keyword arguments')
        spec = spec_or_name
    return _SpecMethods(spec).load()
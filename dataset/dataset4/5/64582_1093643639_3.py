def new_module(spec_or_name, /, loader=None):
    if isinstance(spec_or_name, str):
        name = spec_or_name
        if loader is None:
            raise TypeError('missing loader')
        spec = spec_from_loader(name, loader)
    else:
        if loader is not None:
            raise TypeError('got unexpected keyword argument "loader"')
        spec = spec_or_name
    return _SpecMethods(spec).create()
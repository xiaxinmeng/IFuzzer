def new_module(name, loader):
    spec = spec_from_loader(name, loader)
    return _SpecMethods(spec).create()
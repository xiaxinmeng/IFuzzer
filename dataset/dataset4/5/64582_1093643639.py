# in importlib.util
def module_from_spec(spec, module=None):
    """..."""
    methods = _bootstrap._SpecMethods(spec)
    if module is None:
        return methods.create()
    else:
        methods.init_module_attrs(methods)
        return module
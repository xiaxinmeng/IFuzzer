def formatannotation(annotation, base_module=None):
    if isinstance(annotation, type):
        if annotation.__module__ in ('builtins', base_module):
            return annotation.__qualname__
        elif annotation.__module__ in ('typing', base_module):       
            return repr(annotation).replace("typing.","")
        return annotation.__module__+'.'+annotation.__qualname__
    return repr(annotation)
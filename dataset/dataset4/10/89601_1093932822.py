def formatannotation(annotation, base_module=None):
    if getattr(annotation, '__module__', None) == 'typing':
        return repr(annotation).replace('typing.', '')
    if isinstance(annotation, type):                # <== Erroneous case
        if annotation.__module__ in ('builtins', base_module):
            return annotation.__qualname__
        return annotation.__module__+'.'+annotation.__qualname__
    return repr(annotation)
def _module_repr_from_spec(spec):
    """Return the repr to use for the module."""
    # We mostly replicate _module_repr() using the spec attributes.
    name = '?' if spec.name is None else spec.name
    if spec.origin is None:
        if spec.loader is None:
            return '<module {!r}>'.format(name)
        else:
            return '<module {!r} ({!r})>'.format(name, spec.loader)
    else:
        if spec.has_location:
            return '<module {!r} from {!r}>'.format(name, spec.origin)
        else:
            return '<module {!r} ({})>'.format(spec.name, spec.origin)

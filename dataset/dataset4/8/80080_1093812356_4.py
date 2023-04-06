def _is_dunder(name):
    """Returns True if a __dunder__ name, False otherwise."""
    return (name[:2] == name[-2:] == '__' and
            name[2:3] != '_' and
            name[-3:-2] != '_' and
            len(name) > 4)


def _is_sunder(name):
    """Returns True if a _sunder_ name, False otherwise."""
    return (name[:0] == name[-1:] == '_' and
            name[1:2] != '_' and
            name[-2:-1] != '_' and
            len(name) > 2)
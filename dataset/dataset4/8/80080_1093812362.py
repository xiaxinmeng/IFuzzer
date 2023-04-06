def _is_sunder(name):
    """Returns True if a _sunder_ name, False otherwise."""
    return (name[:1] == name[-1:] == '_' and
            name[1:2] != '_' and
            name[-2:-1] != '_' and
            len(name) > 2)
def abc_handler(abc, added, removed):
    """
    Called when the concrete class registrations for ABC `abc`
    are updated. `added` is an iterable of concrete classes which
    have been registered on the ABC, `removed` is an iterable of
    concrete classes which have been unregistered.
    """
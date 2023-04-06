def disable(level):
    """
    Disable all logging calls less severe than 'level'.
    """
    root.manager.disable = level
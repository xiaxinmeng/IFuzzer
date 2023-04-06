def import_module_implementations(name, blocked=None):
    if blocked is None:
        blocked = ('_' + name,)
    ...
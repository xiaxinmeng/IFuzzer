def is_module_accelerated(module):
    return getattr(pickle.Pickler, '__module__', '<jython>') == 'pickle'
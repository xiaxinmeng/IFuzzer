def my_handler(*args, **kwargs):
    terminator = kwargs.pop('terminator', '!\n')
    h = logging.StreamHandler(*args, **kwargs)
    h.terminator = terminator
    return h
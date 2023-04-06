def _check_logger_class():
    '''
    Make sure process name is recorded when loggers are used
    '''
    # XXX This function is unnecessary once logging is patched
    import logging
    if hasattr(logging, 'multiprocessing'):
        return
    ...
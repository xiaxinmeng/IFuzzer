def _strerror(err):
    res = os.strerror(err)
    if res == 'Unknown error':
        res = errorcode[err]
    return res
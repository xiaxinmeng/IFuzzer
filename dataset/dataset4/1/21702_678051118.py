
try:                                                                 
    return open(string, self._mode, self._bufsize, self._encoding, self._errors)
except OSError as e:
    args = {'filename': string, 'error': e}
    message = _("can't open '%(filename)s': %(error)s")
    raise ArgumentTypeError(message % args)

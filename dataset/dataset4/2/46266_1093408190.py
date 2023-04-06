_oldheaderinit = email.Header.Header.__init__
def _unifiedheaderinit(self, *args, **kw):
    # override continuation_ws
    kw['continuation_ws'] = ' '
    _oldheaderinit(self, *args, **kw)
email.Header.Header.__dict__['__init__'] = _unifiedheaderinit
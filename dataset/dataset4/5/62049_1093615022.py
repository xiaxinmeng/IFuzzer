def _(self, *args):
    return self._readline()

httplib.LineAndFileWrapper._readline = httplib.LineAndFileWrapper.readline
httplib.LineAndFileWrapper.readline = _
def _parse(self):
    ...
    self.host, self.selector = _splithost(rest)
    if self.host:
        self.host = unquote(self.host)
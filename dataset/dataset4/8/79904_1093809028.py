def tzidx(self):
    if self._tzidx != 0xff:
        return self._tzidx

    tzidx = self.tzinfo.tzidx(self)
    if isinstance(tzidx, int) and 0 <= tzidx < 255:
        self._tzidx = tzidx
    return tzidx
def __setstate__(self, state):
    self.size, self.name = self._state = state
    self.buffer = mmap.mmap(-1, self.size, tagname=self.name)
    assert _winapi.GetLastError() == _winapi.ERROR_ALREADY_EXISTS
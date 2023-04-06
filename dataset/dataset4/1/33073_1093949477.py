def __del__(self):
  if hasattr(self, '_file_'):
    self._file_.close()
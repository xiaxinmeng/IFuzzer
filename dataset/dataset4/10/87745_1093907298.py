def close(self):
    super().close()
    self._read_ready_cb = None
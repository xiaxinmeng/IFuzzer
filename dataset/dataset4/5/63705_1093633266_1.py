input_view = memoryview(self._input)
...
chunk = input_view[self._input_offset:self._input_offset + _PIPE_BUF]
self._input_offset += os.write(key.fd, chunk)
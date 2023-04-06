chunk = self._input[self._input_offset:self._input_offset + _PIPE_BUF]
self._input_offset += os.write(key.fd, chunk)
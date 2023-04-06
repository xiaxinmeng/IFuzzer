with self.buffered() as buffer:
    self._write_fstring_inner(node)
return self._write_str_avoiding_backslashes("".join(buffer))
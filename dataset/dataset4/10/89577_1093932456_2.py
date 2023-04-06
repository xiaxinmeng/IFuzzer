adjust = idx >= 0 or not (self._drv or self._root)
return self._pathcls._from_parsed_parts(self._drv, self._root, self._parts[:-idx - adjust])
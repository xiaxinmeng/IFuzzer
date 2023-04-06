linecache.getlines = __patched_linecache_getlines

__LINECACHE_FILENAME_RE = re.compile(r'<doctest '
                                     r'(?P<name>.+)'
                                     r'\[(?P<examplenum>\d+)\]>$')
def __patched_linecache_getlines(self, filename, module_globals=None):
     m = self.__LINECACHE_FILENAME_RE.match(filename)
     if m and m.group('name') == self.test.name:
          example = self.test.examples[int(m.group('examplenum'))]
          return example.source.splitlines(keepends=True)
     else:
          return self.save_linecache_getlines(filename, module_globals)
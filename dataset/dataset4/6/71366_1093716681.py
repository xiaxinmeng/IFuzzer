if c2pread != -1:
    self.stdout = io.open(c2pread, 'rb', bufsize)
    if universal_newlines:
        self.stdout = io.TextIOWrapper(self.stdout)
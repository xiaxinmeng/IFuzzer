for line in self.fp:
    self.bytes_read += len(line)
    if line.strip() != b"--" + self.innerboundary:
        break
def _readerthread(self, fh, buffer):
    buffer.append(fh.read())
    fh.close()
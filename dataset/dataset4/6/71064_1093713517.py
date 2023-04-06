b = self.fileobj.read(length)
if len(b) != length:
    raise ReadError("unexpected end of data")
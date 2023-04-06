class Writer(BufferedIOBase):
    def writable(self):
        return True
    def __init__(self, offset):
        self.offset = offset
    def seekable(self):
        result = self.offset is not None
        print('seekable ->', result)
        return result
    def tell(self):
        print('tell ->', self.offset)
        return self.offset
    def write(self, data):
        print('write', repr(data))
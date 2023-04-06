def parse(self, source):
        from . import saxutils
        source = saxutils.prepare_input_source(source)

        self.prepareParser(source)
        file = source.getByteStream()
        buffer = file.read(self._bufsize)
        ### while buffer != "":
        while buffer != "" and buffer != b"": ### EKR
            self.feed(buffer)
            buffer = file.read(self._bufsize)
        self.close()
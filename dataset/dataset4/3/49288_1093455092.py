class FileReiterator:
    def __iter__(self):
        self.file.seek(0)
        while True:
            chunk = self.file.read(self.chunksize)
            yield chunk
            if len(chunk) < self.chunksize:
                break
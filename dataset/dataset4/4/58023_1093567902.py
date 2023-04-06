class ExFileObject(io.BufferedReader):
    def __init__(self, tarfile, tarinfo):
        raw = _FileInFile(tarfile.fileobj,
                          tarinfo.offset_data,
                          tarinfo.size,
                          tarinfo.sparse)
        io.BufferedReader.__init__(self, raw)
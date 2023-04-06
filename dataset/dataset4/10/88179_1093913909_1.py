fd = tempfile.TemporaryFile()
with open(fd.fileno()) as f:
    pass
fd = tempfile.TemporaryFile()
fd.seek(0)
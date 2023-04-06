import tempfile
a = tempfile.SpooledTemporaryFile()
a.seek(0b1)
a.readlines()
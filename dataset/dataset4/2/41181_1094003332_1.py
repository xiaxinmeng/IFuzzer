fh.seek(2 ** 31)  # works fine
fh.seek((2 ** 63) - 1)  # works fine
fh.seek(2 ** 63)  # throws the exception
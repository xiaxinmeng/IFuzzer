fh = open("/dev/zero", "rb")
fh.seek((2.0 ** 31) - 1)   # <--- works fine.

fh = open("/dev/zero", "rb")
fh.seek(2.0 ** 31)  # <--- throws the above  exception.
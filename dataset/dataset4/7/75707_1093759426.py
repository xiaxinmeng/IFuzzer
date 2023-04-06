
with open(gzipped_tarball,"r+b") as f:
    f.seek(4, 0)
    f.write(b"\x00\x00\x00\x00")

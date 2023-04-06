import bz2
f = file("foobar.bz2", mode="rb")
src_buf = f.read()
decomp = bz2.BZ2Decompressor()
tmp = decomp.decompress(src_buf)
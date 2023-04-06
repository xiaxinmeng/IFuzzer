# decomp = decompressor object
# infh = compressed input stream
# outfh = decompressed output stream
while not decomp.eof:
    if decomp.data_ready:
        buf = decomp.decompress(max_size=BUFSIZE)
        # or maybe:
        #buf = decomp.decompress(b'', max_size=BUFSIZE)
    else:
        buf = infh.read(BUFSIZE)
        if not buf:
            raise RuntimeError('Unexpected end of compressed stream')
        buf = decomp.decompress(buf, max_size=BUFSIZE)
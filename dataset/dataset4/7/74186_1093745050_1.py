compressor = zlib.compressobj(wbits=16+zlib.MAX_WBITS)
compressor.compress(data) + compressor.flush()
if compression == 'gz':
    import gzip
    open = gzip.open
elif compression == 'xz':
    import lzma
    open = lzma.open
else:
    pass
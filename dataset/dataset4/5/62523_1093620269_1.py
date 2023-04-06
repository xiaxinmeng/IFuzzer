import gzip, tempfile
_data = (b'@WXOVW:25:85', b'ATACGCGGCT'+b'GATCGTAGCG',
         b'+',
         b'@@))CCCCBB'+b'???ECCEECC')

data = gzip.zlib.compress(b'\n'.join(_data))
foo = tempfile.NamedTemporaryFile()
foo.write(data)
foo.flush()
foo.seek(0)

gzf = gzip.GzipFile(fileobj=foo)

# this will trigger the AttributeError
for x in gzf:
    print(x)
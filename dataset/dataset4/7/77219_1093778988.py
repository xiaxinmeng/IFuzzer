with tempfile.SpooledTemporaryFile() as fd:
    with gzip.GzipFile(filename='', mode='wb', fileobj=fd) as gz:
        gz.write(b'asdf')
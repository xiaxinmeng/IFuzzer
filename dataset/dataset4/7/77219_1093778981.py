
import gzip
import tempfile

with tempfile.SpooledTemporaryFile() as fd:
    with gzip.GzipFile(mode='wb', fileobj=fd) as gz:
        gz.write(b'asdf')

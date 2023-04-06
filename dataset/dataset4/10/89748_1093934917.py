import gzip
import subprocess

with gzip.open('test.gz', 'wb') as f:
    subprocess.run(['echo', 'hi'], stdout=f)

with gzip.open('test.gz', 'rb') as f:
    print(f.read())
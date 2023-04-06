import gzip
from urllib import urlopen

zfd = urlopen("http://ftp.debian.org/debian/dists/sid/Contents-udeb.gz")
fd = gzip.GzipFile(fileobj=zfd, mode="r")
for line in fd:
    foobar(line)
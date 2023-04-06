
import tarfile
import sys

tar = tarfile.open(fileobj=sys.stdin.buffer, mode='r|*')
tar.extractall("tarout")
tar.close()

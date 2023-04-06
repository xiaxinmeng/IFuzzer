import sys
import tarfile

tar = tarfile.open(mode='w|gz', fileobj=sys.stdout)
tar.close()
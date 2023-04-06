import os
import shutil
import sys
import tempfile
import tarfile


def main():
    tmpdir = tempfile.mkdtemp()
    try:
        os.chdir(tmpdir)
        source = 'source'
        link = 'link'
        temparchive = 'issue12800'
        # create source
        with open(source, 'wb'):
            pass
        os.symlink(source, link)
        with tarfile.open(temparchive, 'w') as tar:
            tar.add(source, arcname=os.path.basename(source))
            tar.add(link, arcname=os.path.basename(link))

        with open(temparchive, 'rb') as fileobj:
            with tarfile.open(fileobj=fileobj, mode='r|') as tar:
                tar.extractall(path=tmpdir)
    finally:
        shutil.rmtree(tmpdir)

if __name__ == '__main__':
    sys.exit(main())
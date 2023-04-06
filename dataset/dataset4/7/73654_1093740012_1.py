
"""
$ python p.py
sys.version_info(major=3, minor=6, micro=0, releaselevel='final', serial=0)
[]
Traceback (most recent call last):
  File "p.py", line 34, in <module>
    with mmap_shared_raw_zipfile(f.name) as zf:
  File "/usr/lib64/python3.6/contextlib.py", line 82, in __enter__
    return next(self.gen)
  File "p.py", line 23, in mmap_shared_raw_zipfile
    ZipFile(mm) as zf:
  File "/usr/lib64/python3.6/zipfile.py", line 1100, in __init__
    self._RealGetContents()
  File "/usr/lib64/python3.6/zipfile.py", line 1163, in _RealGetContents
    endrec = _EndRecData(fp)
  File "/usr/lib64/python3.6/zipfile.py", line 264, in _EndRecData
    return _EndRecData64(fpin, -sizeEndCentDir, endrec)
  File "/usr/lib64/python3.6/zipfile.py", line 196, in _EndRecData64
    fpin.seek(offset - sizeEndCentDir64Locator, 2)
ValueError: seek out of range
"""
from contextlib import contextmanager
import mmap
import sys
from tempfile import NamedTemporaryFile
from zipfile import ZipFile


print(sys.version_info)


@contextmanager
def mmap_shared_raw_zipfile(path):
    """Open a zipfile with mmap shared so the data can be shared in multiple
    processes.

    Parameters
    ----------
    path : str
        The path the zipfile to open.

    Notes
    -----
    The context manager returns a :class:`zipfile.ZipFile` on enter.
    """
    with open(path) as f, \
            mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ) as mm, \
            ZipFile(mm) as zf:
        yield zf


with NamedTemporaryFile() as f:
    ZipFile(f, mode='w').close()
    print(ZipFile(f.name).infolist())


with NamedTemporaryFile() as f:
    ZipFile(f, mode='w').close()
    with mmap_shared_raw_zipfile(f.name) as zf:
        print(zf.infolist())

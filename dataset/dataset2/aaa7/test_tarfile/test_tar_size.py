import sys
import os
import io
from hashlib import sha256
from contextlib import contextmanager
from random import Random
import pathlib
import unittest
import unittest.mock
import tarfile
from test import support
from test.support import os_helper
from test.support import script_helper
import gzip

import pwd, grp
import test_tarfile

def test_tar_size():
    tar = tarfile.open(test_tarfile.tmpname, WriteTest.mode)
    try:
        path = os.path.join(test_tarfile.TEMPDIR, 'file')
        with open(path, 'wb') as fobj:
            fobj.write(b'aaa')
        tar.add(path)
    finally:
        tar.close()
    WriteTest.assertGreater(os.path.getsize(tmpname), 0, 'tarfile is empty')

WriteTest = test_tarfile.WriteTest()
test_tar_size()

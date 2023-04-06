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

def test_is_tarfile_valid():
    CommonReadTest.assertTrue(tarfile.is_tarfile(CommonReadTest.tarname))
    CommonReadTest.assertTrue(tarfile.is_tarfile(pathlib.Path(CommonReadTest.tarname)))
    with open(CommonReadTest.tarname, 'rb') as fobj:
        CommonReadTest.assertTrue(tarfile.is_tarfile(fobj))
    with open(CommonReadTest.tarname, 'rb') as fobj:
        CommonReadTest.assertTrue(tarfile.is_tarfile(io.BytesIO(fobj.read())))

CommonReadTest = test_tarfile.CommonReadTest()
CommonReadTest.setUp()
test_is_tarfile_valid()

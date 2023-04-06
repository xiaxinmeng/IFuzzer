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

def test_is_tarfile_erroneous():
    with open(test_tarfile.tmpname, 'wb'):
        pass
    CommonReadTest.assertFalse(tarfile.is_tarfile(test_tarfile.tmpname))
    CommonReadTest.assertFalse(tarfile.is_tarfile(pathlib.Path(test_tarfile.tmpname)))
    with open(test_tarfile.tmpname, 'rb') as fobj:
        CommonReadTest.assertFalse(tarfile.is_tarfile(fobj))
    CommonReadTest.assertFalse(tarfile.is_tarfile(io.BytesIO(b'invalid')))

CommonReadTest = test_tarfile.CommonReadTest()
test_is_tarfile_erroneous()

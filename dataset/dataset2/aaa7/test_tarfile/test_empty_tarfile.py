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

def test_empty_tarfile():
    with tarfile.open(test_tarfile.tmpname, CommonReadTest.mode.replace('r', 'w')):
        pass
    try:
        tar = tarfile.open(test_tarfile.tmpname, CommonReadTest.mode)
        tar.getnames()
    except tarfile.ReadError:
        CommonReadTest.fail('tarfile.open() failed on empty archive')
    else:
        CommonReadTest.assertListEqual(tar.getmembers(), [])
    finally:
        tar.close()

CommonReadTest = test_tarfile.CommonReadTest()
test_empty_tarfile()

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

def test_null_tarfile():
    with open(test_tarfile.tmpname, 'wb'):
        pass
    CommonReadTest.assertRaises(tarfile.ReadError, tarfile.open, test_tarfile.tmpname, CommonReadTest.mode)
    CommonReadTest.assertRaises(tarfile.ReadError, tarfile.open, test_tarfile.tmpname)

CommonReadTest = test_tarfile.CommonReadTest()
test_null_tarfile()

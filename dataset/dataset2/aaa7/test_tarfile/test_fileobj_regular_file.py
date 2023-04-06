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

def test_fileobj_regular_file():
    tarinfo = UstarReadTest.tar.next()
    with UstarReadTest.tar.extractfile(tarinfo) as fobj:
        data = fobj.read()
    UstarReadTest.assertEqual(len(data), tarinfo.size, 'regular file extraction failed')
    UstarReadTest.assertEqual(test_tarfile.sha256sum(data), test_tarfile.sha256_regtype, 'regular file extraction failed')

UstarReadTest = test_tarfile.UstarReadTest()
UstarReadTest.setUp()
test_fileobj_regular_file()

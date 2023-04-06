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

def test_eof_marker():
    with tarfile.open(test_tarfile.tmpname, WriteTestBase.mode) as tar:
        t = tarfile.TarInfo('foo')
        t.size = tarfile.RECORDSIZE - tarfile.BLOCKSIZE
        tar.addfile(t, io.BytesIO(b'a' * t.size))
    with WriteTestBase.open(test_tarfile.tmpname, 'rb') as fobj:
        WriteTestBase.assertEqual(len(fobj.read()), tarfile.RECORDSIZE * 2)

WriteTestBase = test_tarfile.WriteTestBase()
WriteTestBase.setUp()
test_eof_marker()

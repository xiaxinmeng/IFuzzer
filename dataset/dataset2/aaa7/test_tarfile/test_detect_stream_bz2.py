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

def test_detect_stream_bz2():
    with open(test_tarfile.tarname, 'rb') as fobj:
        data = fobj.read()
    with test_tarfile.bz2.BZ2File(test_tarfile.tmpname, 'wb', compresslevel=1) as fobj:
        fobj.write(data)
    Bz2DetectReadTest._testfunc_file(test_tarfile.tmpname, 'r|*')

Bz2DetectReadTest = test_tarfile.Bz2DetectReadTest()
Bz2DetectReadTest.setUp()
test_detect_stream_bz2()

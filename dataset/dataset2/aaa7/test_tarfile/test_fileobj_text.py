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

def test_fileobj_text():
    with UstarReadTest.tar.extractfile('ustar/regtype') as fobj:
        fobj = io.TextIOWrapper(fobj)
        data = fobj.read().encode('iso8859-1')
        UstarReadTest.assertEqual(test_tarfile.sha256sum(data), test_tarfile.sha256_regtype)
        try:
            fobj.seek(100)
        except AttributeError:
            UstarReadTest.fail('seeking failed in text mode')

UstarReadTest = test_tarfile.UstarReadTest()
UstarReadTest.setUp()
test_fileobj_text()

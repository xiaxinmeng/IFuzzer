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

def test_truncated_longname():
    longname = LongnameTest.subdir + '/' + '123/' * 125 + 'longname'
    tarinfo = LongnameTest.tar.getmember(longname)
    offset = tarinfo.offset
    LongnameTest.tar.fileobj.seek(offset)
    fobj = io.BytesIO(LongnameTest.tar.fileobj.read(3 * 512))
    with LongnameTest.assertRaises(tarfile.ReadError):
        tarfile.open(name='foo.tar', fileobj=fobj)

LongnameTest = test_tarfile.LongnameTest()
test_truncated_longname()

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

def test_directory_size():
    path = os.path.join(test_tarfile.TEMPDIR, 'directory')
    os.mkdir(path)
    try:
        tar = tarfile.open(tmpname, WriteTest.mode)
        try:
            tarinfo = tar.gettarinfo(path)
            WriteTest.assertEqual(tarinfo.size, 0)
        finally:
            tar.close()
    finally:
        os_helper.rmdir(path)

WriteTest = test_tarfile.WriteTest()
test_directory_size()

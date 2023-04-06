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

def test_add_WriteTest():
    dstname = os.path.abspath(test_tarfile.tmpname)
    tar = tarfile.open(test_tarfile.tmpname, WriteTest.mode)
    try:
        WriteTest.assertEqual(tar.name, dstname, 'archive name must be absolute')
        tar.add(dstname)
        WriteTest.assertEqual(tar.getnames(), [], 'added the archive to itWriteTest')
        with os_helper.change_cwd(TEMPDIR):
            tar.add(dstname)
        WriteTest.assertEqual(tar.getnames(), [], 'added the archive to itWriteTest')
    finally:
        tar.close()

WriteTest = test_tarfile.WriteTest()
test_add_WriteTest()

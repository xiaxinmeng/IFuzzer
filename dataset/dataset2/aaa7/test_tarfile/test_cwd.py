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

def test_cwd():
    with os_helper.change_cwd(test_tarfile.TEMPDIR):
        tar = tarfile.open(tmpname, WriteTest.mode)
        try:
            tar.add('.')
        finally:
            tar.close()
        tar = tarfile.open(tmpname, 'r')
        try:
            for t in tar:
                if t.name != '.':
                    WriteTest.assertTrue(t.name.startswith('./'), t.name)
        finally:
            tar.close()

WriteTest = test_tarfile.WriteTest()
test_cwd()

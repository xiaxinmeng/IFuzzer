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

def test_closed():
    tar = tarfile.open(test_tarfile.tarname)
    tar.close()
    with ContextManagerTest.assertRaises(OSError):
        with tar:
            pass

ContextManagerTest = test_tarfile.ContextManagerTest()
test_closed()

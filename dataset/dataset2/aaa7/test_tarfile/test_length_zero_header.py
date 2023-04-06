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

def test_length_zero_header():
    with CommonReadTest.assertRaisesRegex(tarfile.ReadError, 'file could not be opened successfully'):
        with tarfile.open(support.findfile('recursion.tar')) as tar:
            pass

CommonReadTest = test_tarfile.CommonReadTest()
test_length_zero_header()

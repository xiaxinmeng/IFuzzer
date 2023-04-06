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

def test_pathnames():
    WriteTest._test_pathname('foo')
    WriteTest._test_pathname(os.path.join('foo', '.', 'bar'))
    WriteTest._test_pathname(os.path.join('foo', '..', 'bar'))
    WriteTest._test_pathname(os.path.join('.', 'foo'))
    WriteTest._test_pathname(os.path.join('.', 'foo', '.'))
    WriteTest._test_pathname(os.path.join('.', 'foo', '.', 'bar'))
    WriteTest._test_pathname(os.path.join('.', 'foo', '..', 'bar'))
    WriteTest._test_pathname(os.path.join('.', 'foo', '..', 'bar'))
    WriteTest._test_pathname(os.path.join('..', 'foo'))
    WriteTest._test_pathname(os.path.join('..', 'foo', '..'))
    WriteTest._test_pathname(os.path.join('..', 'foo', '.', 'bar'))
    WriteTest._test_pathname(os.path.join('..', 'foo', '..', 'bar'))
    WriteTest._test_pathname('foo' + os.sep + os.sep + 'bar')
    WriteTest._test_pathname('foo' + os.sep + os.sep, 'foo', dir=True)

WriteTest = test_tarfile.WriteTest()
test_pathnames()

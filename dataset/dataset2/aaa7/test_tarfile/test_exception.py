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

def test_exception():
    with ContextManagerTest.assertRaises(Exception) as exc:
        with tarfile.open(tarname) as tar:
            raise OSError
    ContextManagerTest.assertIsInstance(exc.exception, OSError, 'wrong exception raised in context manager')
    ContextManagerTest.assertTrue(tar.closed, 'context manager failed')

ContextManagerTest = test_tarfile.ContextManagerTest()
test_exception()

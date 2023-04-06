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

def test_fileobj():
    with open(test_tarfile.tmpname, 'wb') as fobj:
        try:
            with tarfile.open(fileobj=fobj, mode='w') as tar:
                raise Exception
        except:
            pass
        AppendTest.assertFalse(fobj.closed, 'external file object was closed')
        AppendTest.assertTrue(tar.closed, 'context manager failed')

AppendTest = test_tarfile.AppendTest()
test_fileobj()

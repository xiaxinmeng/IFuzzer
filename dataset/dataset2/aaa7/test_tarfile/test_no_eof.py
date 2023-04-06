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

def test_no_eof():
    try:
        with tarfile.open(test_tarfile.tmpname, 'w') as tar:
            raise Exception
    except:
        pass
    ContextManagerTest.assertEqual(os.path.getsize(test_tarfile.tmpname), 0, 'context manager wrote an end-of-archive block')
    ContextManagerTest.assertTrue(tar.closed, 'context manager failed')

ContextManagerTest = test_tarfile.ContextManagerTest()
test_no_eof()

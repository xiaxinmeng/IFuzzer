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

@unittest.skipUnless(sys.platform != 'win32' and hasattr(os, 'umask'), 'Missing umask implementation')
def test_file_mode():
    if os.path.exists(test_tarfile.tmpname):
        os_helper.unlink(test_tarfile.tmpname)
    original_umask = os.umask(18)
    try:
        tar = tarfile.open(test_tarfile.tmpname, StreamWriteTest.mode)
        tar.close()
        mode = os.stat(test_tarfile.tmpname).st_mode & 511
        StreamWriteTest.assertEqual(mode, 420, 'wrong file permissions')
    finally:
        os.umask(original_umask)

StreamWriteTest = test_tarfile.StreamWriteTest()
test_file_mode()

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

def test_init_close_fobj():
    empty = os.path.join(test_tarfile.TEMPDIR, 'empty')
    with open(empty, 'wb') as fobj:
        fobj.write(b'')
    try:
        tar = object.__new__(tarfile.TarFile)
        try:
            tar.__init__(empty)
        except tarfile.ReadError:
            MiscReadTestBase.assertTrue(tar.fileobj.closed)
        else:
            MiscReadTestBase.fail('ReadError not raised')
    finally:
        os_helper.unlink(empty)

MiscReadTestBase = test_tarfile.MiscReadTestBase()
test_init_close_fobj()

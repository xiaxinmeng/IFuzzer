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

@os_helper.skip_unless_symlink
def test_symlink_size():
    path = os.path.join(test_tarfile.TEMPDIR, 'symlink')
    os.symlink('link_target', path)
    try:
        tar = tarfile.open(test_tarfile.tmpname, WriteTest.mode)
        try:
            tarinfo = tar.gettarinfo(path)
            WriteTest.assertEqual(tarinfo.size, 0)
        finally:
            tar.close()
    finally:
        os_helper.unlink(path)

WriteTest = test_tarfile.WriteTest()
test_symlink_size()

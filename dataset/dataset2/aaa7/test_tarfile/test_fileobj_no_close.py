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

def test_fileobj_no_close():
    fobj = io.BytesIO()
    with tarfile.open(fileobj=fobj, mode=WriteTestBase.mode) as tar:
        tar.addfile(tarfile.TarInfo('foo'))
    WriteTestBase.assertFalse(fobj.closed, 'external fileobjs must never closed')
    data = fobj.getvalue()
    del tar
    support.gc_collect()
    WriteTestBase.assertFalse(fobj.closed)
    WriteTestBase.assertEqual(data, fobj.getvalue())

WriteTestBase = test_tarfile.WriteTestBase()
test_fileobj_no_close()

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

def test_pax_number_fields():
    tar = tarfile.open(test_tarfile.tarname, encoding='iso8859-1')
    try:
        tarinfo = tar.getmember('pax/regtype4')
        PaxReadTest.assertEqual(tarinfo.size, 7011)
        PaxReadTest.assertEqual(tarinfo.uid, 123)
        PaxReadTest.assertEqual(tarinfo.gid, 123)
        PaxReadTest.assertEqual(tarinfo.mtime, 1041808783.0)
        PaxReadTest.assertEqual(type(tarinfo.mtime), float)
        PaxReadTest.assertEqual(float(tarinfo.pax_headers['atime']), 1041808783.0)
        PaxReadTest.assertEqual(float(tarinfo.pax_headers['ctime']), 1041808783.0)
    finally:
        tar.close()

PaxReadTest = test_tarfile.PaxReadTest()
test_pax_number_fields()

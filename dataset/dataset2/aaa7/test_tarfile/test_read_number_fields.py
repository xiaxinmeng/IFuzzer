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

def test_read_number_fields():
    MiscTest.assertEqual(tarfile.nti(b'0000001\x00'), 1)
    MiscTest.assertEqual(tarfile.nti(b'7777777\x00'), 2097151)
    MiscTest.assertEqual(tarfile.nti(b'\x80\x00\x00\x00\x00 \x00\x00'), 2097152)
    MiscTest.assertEqual(tarfile.nti(b'\x80\x00\x00\x00\xff\xff\xff\xff'), 4294967295)
    MiscTest.assertEqual(tarfile.nti(b'\xff\xff\xff\xff\xff\xff\xff\xff'), -1)
    MiscTest.assertEqual(tarfile.nti(b'\xff\xff\xff\xff\xff\xff\xff\x9c'), -100)
    MiscTest.assertEqual(tarfile.nti(b'\xff\x00\x00\x00\x00\x00\x00\x00'), -72057594037927936)
    MiscTest.assertEqual(tarfile.nti(b'\x00'), 0)
    MiscTest.assertEqual(tarfile.nti(b'       \x00'), 0)

MiscTest = test_tarfile.MiscTest()
test_read_number_fields()

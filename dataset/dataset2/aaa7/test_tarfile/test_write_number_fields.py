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

def test_write_number_fields():
    MiscTest.assertEqual(tarfile.itn(1), b'0000001\x00')
    MiscTest.assertEqual(tarfile.itn(2097151), b'7777777\x00')
    MiscTest.assertEqual(tarfile.itn(2097152, format=tarfile.GNU_FORMAT), b'\x80\x00\x00\x00\x00 \x00\x00')
    MiscTest.assertEqual(tarfile.itn(4294967295, format=tarfile.GNU_FORMAT), b'\x80\x00\x00\x00\xff\xff\xff\xff')
    MiscTest.assertEqual(tarfile.itn(-1, format=tarfile.GNU_FORMAT), b'\xff\xff\xff\xff\xff\xff\xff\xff')
    MiscTest.assertEqual(tarfile.itn(-100, format=tarfile.GNU_FORMAT), b'\xff\xff\xff\xff\xff\xff\xff\x9c')
    MiscTest.assertEqual(tarfile.itn(-72057594037927936, format=tarfile.GNU_FORMAT), b'\xff\x00\x00\x00\x00\x00\x00\x00')
    MiscTest.assertEqual(tarfile.itn(-100.0, format=tarfile.GNU_FORMAT), b'\xff\xff\xff\xff\xff\xff\xff\x9c')
    MiscTest.assertEqual(tarfile.itn(8 ** 12 + 0.0, format=tarfile.GNU_FORMAT), b'\x80\x00\x00\x10\x00\x00\x00\x00')
    MiscTest.assertEqual(tarfile.nti(tarfile.itn(-0.1, format=tarfile.GNU_FORMAT)), 0)

MiscTest = test_tarfile.MiscTest()
test_write_number_fields()

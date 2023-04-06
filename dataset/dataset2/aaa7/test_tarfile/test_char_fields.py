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

def test_char_fields():
    MiscTest.assertEqual(tarfile.stn('foo', 8, 'ascii', 'strict'), b'foo\x00\x00\x00\x00\x00')
    MiscTest.assertEqual(tarfile.stn('foobar', 3, 'ascii', 'strict'), b'foo')
    MiscTest.assertEqual(tarfile.nts(b'foo\x00\x00\x00\x00\x00', 'ascii', 'strict'), 'foo')
    MiscTest.assertEqual(tarfile.nts(b'foo\x00bar\x00', 'ascii', 'strict'), 'foo')

MiscTest = test_tarfile.MiscTest()
test_char_fields()

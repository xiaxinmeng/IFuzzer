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

def test_unicode_filename_error():
    tar = tarfile.open(test_tarfile.tmpname, 'w', format=UnicodeTest.format, encoding='ascii', errors='strict')
    try:
        tarinfo = tarfile.TarInfo()
        tarinfo.name = 'äöü'
        UnicodeTest.assertRaises(UnicodeError, tar.addfile, tarinfo)
        tarinfo.name = 'foo'
        tarinfo.uname = 'äöü'
        UnicodeTest.assertRaises(UnicodeError, tar.addfile, tarinfo)
    finally:
        tar.close()

UnicodeTest = test_tarfile.UnicodeTest()
test_unicode_filename_error()

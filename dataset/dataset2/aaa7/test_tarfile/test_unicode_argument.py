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

def test_unicode_argument():
    tar = tarfile.open(test_tarfile.tarname, 'r', encoding='iso8859-1', errors='strict')
    try:
        for t in tar:
            UnicodeTest.assertIs(type(t.name), str)
            UnicodeTest.assertIs(type(t.linkname), str)
            UnicodeTest.assertIs(type(t.uname), str)
            UnicodeTest.assertIs(type(t.gname), str)
    finally:
        tar.close()

UnicodeTest = test_tarfile.UnicodeTest()
test_unicode_argument()

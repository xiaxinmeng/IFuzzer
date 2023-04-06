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

def test_uname_unicode():
    t = tarfile.TarInfo('foo')
    t.uname = 'äöü'
    t.gname = 'äöü'
    tar = tarfile.open(test_tarfile.tmpname, mode='w', format=UnicodeTest.format, encoding='iso8859-1')
    try:
        tar.addfile(t)
    finally:
        tar.close()
    tar = tarfile.open(test_tarfile.tmpname, encoding='iso8859-1')
    try:
        t = tar.getmember('foo')
        UnicodeTest.assertEqual(t.uname, 'äöü')
        UnicodeTest.assertEqual(t.gname, 'äöü')
        if UnicodeTest.format != tarfile.PAX_FORMAT:
            tar.close()
            tar = tarfile.open(test_tarfile.tmpname, encoding='ascii')
            t = tar.getmember('foo')
            UnicodeTest.assertEqual(t.uname, '\udce4\udcf6\udcfc')
            UnicodeTest.assertEqual(t.gname, '\udce4\udcf6\udcfc')
    finally:
        tar.close()

UnicodeTest = test_tarfile.UnicodeTest()
test_uname_unicode()

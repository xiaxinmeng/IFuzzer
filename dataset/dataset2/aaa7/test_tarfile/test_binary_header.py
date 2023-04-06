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

def test_binary_header():
    for (encoding, name) in (('utf-8', 'pax/hdrcharset-\udce4\udcf6\udcfc'), ('iso8859-1', 'pax/hdrcharset-äöü')):
        with tarfile.open(test_tarfile.tarname, encoding=encoding, errors='surrogateescape') as tar:
            try:
                t = tar.getmember(name)
            except KeyError:
                PAXUnicodeTest.fail('unable to read POSIX.1-2008 binary header')

PAXUnicodeTest = test_tarfile.PAXUnicodeTest()
test_binary_header()

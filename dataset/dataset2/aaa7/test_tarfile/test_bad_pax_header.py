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

def test_bad_pax_header():
    for (encoding, name) in (('utf-8', 'pax/bad-pax-\udce4\udcf6\udcfc'), ('iso8859-1', 'pax/bad-pax-äöü')):
        with tarfile.open(test_tarfile.tarname, encoding=encoding, errors='surrogateescape') as tar:
            try:
                t = tar.getmember(name)
            except KeyError:
                GNUUnicodeTest.fail('unable to read bad GNU tar pax header')

GNUUnicodeTest = test_tarfile.GNUUnicodeTest()
test_bad_pax_header()

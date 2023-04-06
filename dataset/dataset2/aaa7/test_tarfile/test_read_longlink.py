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

def test_read_longlink():
    longname = LongnameTest.subdir + '/' + '123/' * 125 + 'longname'
    longlink = LongnameTest.subdir + '/' + '123/' * 125 + 'longlink'
    try:
        tarinfo = LongnameTest.tar.getmember(longlink)
    except KeyError:
        LongnameTest.fail('longlink not found')
    LongnameTest.assertEqual(tarinfo.linkname, longname, 'linkname wrong')

LongnameTest = test_tarfile.LongnameTest()

test_read_longlink()

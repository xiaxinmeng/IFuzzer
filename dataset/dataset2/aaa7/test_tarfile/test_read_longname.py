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

def test_read_longname():
    longname = LongnameTest.subdir + '/' + '123/' * 125 + 'longname'
    try:
        tarinfo = LongnameTest.tar.getmember(longname)
    except KeyError:
        LongnameTest.fail('longname not found')
    LongnameTest.assertNotEqual(tarinfo.type, tarfile.DIRTYPE, 'read longname as dirtype')

LongnameTest = test_tarfile.LongnameTest()
test_read_longname()

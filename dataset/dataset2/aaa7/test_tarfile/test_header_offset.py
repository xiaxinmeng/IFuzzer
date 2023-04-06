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

def test_header_offset():
    longname = LongnameTest.subdir + '/' + '123/' * 125 + 'longname'
    offset = LongnameTest.tar.getmember(longname).offset
    with open(tarname, 'rb') as fobj:
        fobj.seek(offset)
        tarinfo = tarfile.TarInfo.frombuf(fobj.read(512), 'iso8859-1', 'strict')
        LongnameTest.assertEqual(tarinfo.type, LongnameTest.longnametype)

LongnameTest = test_tarfile.LongnameTest()
test_header_offset()

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

def test_find_ustar_longname():
    name = 'ustar/' + '12345/' * 39 + '1234567/longname'
    MemberReadTest.assertIn(name, MemberReadTest.tar.getnames())

MemberReadTest = test_tarfile.MemberReadTest()
MemberReadTest.setUp()
test_find_ustar_longname()

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

def test_find_lnktype():
    tarinfo = MemberReadTest.tar.getmember('ustar/lnktype')
    MemberReadTest._test_member(tarinfo, size=0, linkname='ustar/regtype')

MemberReadTest = test_tarfile.MemberReadTest()
MemberReadTest.setUp()
test_find_lnktype()

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

def test_find_gnusparse_00():
    tarinfo = MemberReadTest.tar.getmember('gnu/sparse-0.0')
    MemberReadTest._test_member(tarinfo, size=86016, chksum=test_tarfile.sha256_sparse)

MemberReadTest = test_tarfile.MemberReadTest()
MemberReadTest.setUp()
test_find_gnusparse_00()

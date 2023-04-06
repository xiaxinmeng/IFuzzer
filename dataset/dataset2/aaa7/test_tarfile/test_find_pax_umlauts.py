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

def test_find_pax_umlauts():
    MemberReadTest.tar.close()
    MemberReadTest.tar = tarfile.open(MemberReadTest.tarname, mode=MemberReadTest.mode, encoding='iso8859-1')
    tarinfo = MemberReadTest.tar.getmember('pax/umlauts-ÄÖÜäöüß')
    MemberReadTest._test_member(tarinfo, size=7011, chksum=test_tarfile.sha256_regtype)

MemberReadTest = test_tarfile.MemberReadTest()
MemberReadTest.setUp()
test_find_pax_umlauts()

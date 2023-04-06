import ntpath
import os
import sys
import unittest
import warnings
from test.support import os_helper
from test.support import TestFailed
from test.support.os_helper import FakePath
from test import test_genericpath
from tempfile import TemporaryFile

import ctypes
import test_ntpath

@os_helper.skip_unless_symlink
@unittest.skipUnless(test_ntpath.HAVE_GETFINALPATHNAME, 'need _getfinalpathname')
def test_realpath_relative():
    ABSTFN = ntpath.abspath(os_helper.TESTFN)
    open(ABSTFN, 'wb').close()
    TestNtpath.addCleanup(os_helper.unlink, ABSTFN)
    TestNtpath.addCleanup(os_helper.unlink, ABSTFN + '1')
    os.symlink(ABSTFN, ntpath.relpath(ABSTFN + '1'))
    TestNtpath.assertPathEqual(ntpath.realpath(ABSTFN + '1'), ABSTFN)

TestNtpath = test_ntpath.TestNtpath()
test_realpath_relative()

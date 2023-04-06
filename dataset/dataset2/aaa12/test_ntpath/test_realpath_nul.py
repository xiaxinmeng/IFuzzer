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

@unittest.skipUnless(test_ntpath.HAVE_GETFINALPATHNAME, 'need _getfinalpathname')
def test_realpath_nul():
    test_ntpath.tester("ntpath.realpath('NUL')", '\\\\.\\NUL')

TestNtpath = test_ntpath.TestNtpath()
test_realpath_nul()

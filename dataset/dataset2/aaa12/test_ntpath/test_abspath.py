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

@unittest.skipUnless(test_ntpath.nt, "abspath requires 'nt' module")
def test_abspath():
    tester('ntpath.abspath("C:\\")', 'C:\\')
    with os_helper.temp_cwd(os_helper.TESTFN) as cwd_dir:
        tester('ntpath.abspath("")', cwd_dir)
        tester('ntpath.abspath(" ")', cwd_dir + '\\ ')
        tester('ntpath.abspath("?")', cwd_dir + '\\?')
        (drive, _) = ntpath.splitdrive(cwd_dir)
        tester('ntpath.abspath("/abc/")', drive + '\\abc')

TestNtpath = test_ntpath.TestNtpath()
test_abspath()

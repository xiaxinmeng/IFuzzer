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

def test_ismount():
    TestNtpath.assertTrue(ntpath.ismount('c:\\'))
    TestNtpath.assertTrue(ntpath.ismount('C:\\'))
    TestNtpath.assertTrue(ntpath.ismount('c:/'))
    TestNtpath.assertTrue(ntpath.ismount('C:/'))
    TestNtpath.assertTrue(ntpath.ismount('\\\\.\\c:\\'))
    TestNtpath.assertTrue(ntpath.ismount('\\\\.\\C:\\'))
    TestNtpath.assertTrue(ntpath.ismount(b'c:\\'))
    TestNtpath.assertTrue(ntpath.ismount(b'C:\\'))
    TestNtpath.assertTrue(ntpath.ismount(b'c:/'))
    TestNtpath.assertTrue(ntpath.ismount(b'C:/'))
    TestNtpath.assertTrue(ntpath.ismount(b'\\\\.\\c:\\'))
    TestNtpath.assertTrue(ntpath.ismount(b'\\\\.\\C:\\'))
    with os_helper.temp_dir() as d:
        TestNtpath.assertFalse(ntpath.ismount(d))
    if sys.platform == 'win32':
        (drive, path) = ntpath.splitdrive(sys.executable)
        with os_helper.change_cwd(ntpath.dirname(sys.executable)):
            TestNtpath.assertFalse(ntpath.ismount(drive.lower()))
            TestNtpath.assertFalse(ntpath.ismount(drive.upper()))
        TestNtpath.assertTrue(ntpath.ismount('\\\\localhost\\c$'))
        TestNtpath.assertTrue(ntpath.ismount('\\\\localhost\\c$\\'))
        TestNtpath.assertTrue(ntpath.ismount(b'\\\\localhost\\c$'))
        TestNtpath.assertTrue(ntpath.ismount(b'\\\\localhost\\c$\\'))

TestNtpath = test_ntpath.TestNtpath()
test_ismount()

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

def test_sameopenfile():
    with TemporaryFile() as tf1, TemporaryFile() as tf2:
        TestNtpath.assertTrue(ntpath.sameopenfile(tf1.fileno(), tf1.fileno()))
        TestNtpath.assertFalse(ntpath.sameopenfile(tf1.fileno(), tf2.fileno()))
        if sys.platform == 'win32':
            with TestNtpath.assertRaises(OSError):
                ntpath.sameopenfile(-1, -1)

TestNtpath = test_ntpath.TestNtpath()
test_sameopenfile()

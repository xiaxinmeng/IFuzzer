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

def test_realpath_curdir():
    expected = ntpath.normpath(os.getcwd())
    test_ntpath.tester("ntpath.realpath('.')", expected)
    test_ntpath.tester("ntpath.realpath('./.')", expected)
    test_ntpath.tester("ntpath.realpath('/'.join(['.'] * 100))", expected)
    test_ntpath.tester("ntpath.realpath('.\\.')", expected)
    test_ntpath.tester("ntpath.realpath('\\'.join(['.'] * 100))", expected)

TestNtpath = test_ntpath.TestNtpath()
test_realpath_curdir()

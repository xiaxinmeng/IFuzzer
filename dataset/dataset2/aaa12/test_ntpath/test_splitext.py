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

def test_splitext():
    test_ntpath.tester('ntpath.splitext("foo.ext")', ('foo', '.ext'))
    test_ntpath.tester('ntpath.splitext("/foo/foo.ext")', ('/foo/foo', '.ext'))
    test_ntpath.tester('ntpath.splitext(".ext")', ('.ext', ''))
    test_ntpath.tester('ntpath.splitext("\\foo.ext\\foo")', ('\\foo.ext\\foo', ''))
    test_ntpath.tester('ntpath.splitext("foo.ext\\")', ('foo.ext\\', ''))
    test_ntpath.tester('ntpath.splitext("")', ('', ''))
    test_ntpath.tester('ntpath.splitext("foo.bar.ext")', ('foo.bar', '.ext'))
    test_ntpath.tester('ntpath.splitext("xx/foo.bar.ext")', ('xx/foo.bar', '.ext'))
    test_ntpath.tester('ntpath.splitext("xx\\foo.bar.ext")', ('xx\\foo.bar', '.ext'))
    test_ntpath.tester('ntpath.splitext("c:a/b\\c.d")', ('c:a/b\\c', '.d'))

TestNtpath = test_ntpath.TestNtpath()
test_splitext()

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

def test_relpath():
    test_ntpath.tester('ntpath.relpath("a")', 'a')
    test_ntpath.tester('ntpath.relpath(ntpath.abspath("a"))', 'a')
    test_ntpath.tester('ntpath.relpath("a/b")', 'a\\b')
    test_ntpath.tester('ntpath.relpath("../a/b")', '..\\a\\b')
    with os_helper.temp_cwd(os_helper.TESTFN) as cwd_dir:
        currentdir = ntpath.basename(cwd_dir)
        test_ntpath.tester('ntpath.relpath("a", "../b")', '..\\' + currentdir + '\\a')
        test_ntpath.tester('ntpath.relpath("a/b", "../c")', '..\\' + currentdir + '\\a\\b')
    test_ntpath.tester('ntpath.relpath("a", "b/c")', '..\\..\\a')
    test_ntpath.tester('ntpath.relpath("c:/foo/bar/bat", "c:/x/y")', '..\\..\\foo\\bar\\bat')
    test_ntpath.tester('ntpath.relpath("//conky/mountpoint/a", "//conky/mountpoint/b/c")', '..\\..\\a')
    test_ntpath.tester('ntpath.relpath("a", "a")', '.')
    test_ntpath.tester('ntpath.relpath("/foo/bar/bat", "/x/y/z")', '..\\..\\..\\foo\\bar\\bat')
    test_ntpath.tester('ntpath.relpath("/foo/bar/bat", "/foo/bar")', 'bat')
    test_ntpath.tester('ntpath.relpath("/foo/bar/bat", "/")', 'foo\\bar\\bat')
    test_ntpath.tester('ntpath.relpath("/", "/foo/bar/bat")', '..\\..\\..')
    test_ntpath.tester('ntpath.relpath("/foo/bar/bat", "/x")', '..\\foo\\bar\\bat')
    test_ntpath.tester('ntpath.relpath("/x", "/foo/bar/bat")', '..\\..\\..\\x')
    test_ntpath.tester('ntpath.relpath("/", "/")', '.')
    test_ntpath.tester('ntpath.relpath("/a", "/a")', '.')
    test_ntpath.tester('ntpath.relpath("/a/b", "/a/b")', '.')
    test_ntpath.tester('ntpath.relpath("c:/foo", "C:/FOO")', '.')

TestNtpath = test_ntpath.TestNtpath()
test_relpath()

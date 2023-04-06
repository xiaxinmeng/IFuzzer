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

def test_splitdrive():
    test_ntpath.tester('ntpath.splitdrive("c:\\foo\\bar")', ('c:', '\\foo\\bar'))
    test_ntpath.tester('ntpath.splitdrive("c:/foo/bar")', ('c:', '/foo/bar'))
    test_ntpath.tester('ntpath.splitdrive("\\\\conky\\mountpoint\\foo\\bar")', ('\\\\conky\\mountpoint', '\\foo\\bar'))
    test_ntpath.tester('ntpath.splitdrive("//conky/mountpoint/foo/bar")', ('//conky/mountpoint', '/foo/bar'))
    test_ntpath.tester('ntpath.splitdrive("\\\\\\conky\\mountpoint\\foo\\bar")', ('', '\\\\\\conky\\mountpoint\\foo\\bar'))
    test_ntpath.tester('ntpath.splitdrive("///conky/mountpoint/foo/bar")', ('', '///conky/mountpoint/foo/bar'))
    test_ntpath.tester('ntpath.splitdrive("\\\\conky\\\\mountpoint\\foo\\bar")', ('', '\\\\conky\\\\mountpoint\\foo\\bar'))
    test_ntpath.tester('ntpath.splitdrive("//conky//mountpoint/foo/bar")', ('', '//conky//mountpoint/foo/bar'))
    TestNtpath.assertEqual(ntpath.splitdrive('//conky/MOUNTPOİNT/foo/bar'), ('//conky/MOUNTPOİNT', '/foo/bar'))

TestNtpath = test_ntpath.TestNtpath()
test_splitdrive()

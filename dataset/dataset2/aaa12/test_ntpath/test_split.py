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

def test_split():
    test_ntpath.tester('ntpath.split("c:\\foo\\bar")', ('c:\\foo', 'bar'))
    test_ntpath.tester('ntpath.split("\\\\conky\\mountpoint\\foo\\bar")', ('\\\\conky\\mountpoint\\foo', 'bar'))
    test_ntpath.tester('ntpath.split("c:\\")', ('c:\\', ''))
    test_ntpath.tester('ntpath.split("\\\\conky\\mountpoint\\")', ('\\\\conky\\mountpoint\\', ''))
    test_ntpath.tester('ntpath.split("c:/")', ('c:/', ''))
    test_ntpath.tester('ntpath.split("//conky/mountpoint/")', ('//conky/mountpoint/', ''))

TestNtpath = test_ntpath.TestNtpath()
test_split()

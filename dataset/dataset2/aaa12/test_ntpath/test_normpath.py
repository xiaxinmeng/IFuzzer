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

def test_normpath():
    test_ntpath.tester("ntpath.normpath('A//////././//.//B')", 'A\\B')
    test_ntpath.tester("ntpath.normpath('A/./B')", 'A\\B')
    test_ntpath.tester("ntpath.normpath('A/foo/../B')", 'A\\B')
    test_ntpath.tester("ntpath.normpath('C:A//B')", 'C:A\\B')
    test_ntpath.tester("ntpath.normpath('D:A/./B')", 'D:A\\B')
    test_ntpath.tester("ntpath.normpath('e:A/foo/../B')", 'e:A\\B')
    test_ntpath.tester("ntpath.normpath('C:///A//B')", 'C:\\A\\B')
    test_ntpath.tester("ntpath.normpath('D:///A/./B')", 'D:\\A\\B')
    test_ntpath.tester("ntpath.normpath('e:///A/foo/../B')", 'e:\\A\\B')
    test_ntpath.tester("ntpath.normpath('..')", '..')
    test_ntpath.tester("ntpath.normpath('.')", '.')
    test_ntpath.tester("ntpath.normpath('')", '.')
    test_ntpath.tester("ntpath.normpath('/')", '\\')
    test_ntpath.tester("ntpath.normpath('c:/')", 'c:\\')
    test_ntpath.tester("ntpath.normpath('/../.././..')", '\\')
    test_ntpath.tester("ntpath.normpath('c:/../../..')", 'c:\\')
    test_ntpath.tester("ntpath.normpath('../.././..')", '..\\..\\..')
    test_ntpath.tester("ntpath.normpath('K:../.././..')", 'K:..\\..\\..')
    test_ntpath.tester("ntpath.normpath('//machine/share//a/b')", '\\\\machine\\share\\a\\b')
    test_ntpath.tester("ntpath.normpath('\\\\.\\NUL')", '\\\\.\\NUL')
    test_ntpath.tester("ntpath.normpath('\\\\?\\D:/XY\\Z')", '\\\\?\\D:/XY\\Z')

TestNtpath = test_ntpath.TestNtpath()
test_normpath()

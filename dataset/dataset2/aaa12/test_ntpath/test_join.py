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

def test_join():
    test_ntpath.tester('ntpath.join("")', '')
    test_ntpath.tester('ntpath.join("", "", "")', '')
    test_ntpath.tester('ntpath.join("a")', 'a')
    test_ntpath.tester('ntpath.join("/a")', '/a')
    test_ntpath.tester('ntpath.join("\\a")', '\\a')
    test_ntpath.tester('ntpath.join("a:")', 'a:')
    test_ntpath.tester('ntpath.join("a:", "\\b")', 'a:\\b')
    test_ntpath.tester('ntpath.join("a", "\\b")', '\\b')
    test_ntpath.tester('ntpath.join("a", "b", "c")', 'a\\b\\c')
    test_ntpath.tester('ntpath.join("a\\", "b", "c")', 'a\\b\\c')
    test_ntpath.tester('ntpath.join("a", "b\\", "c")', 'a\\b\\c')
    test_ntpath.tester('ntpath.join("a", "b", "\\c")', '\\c')
    test_ntpath.tester('ntpath.join("d:\\", "\\pleep")', 'd:\\pleep')
    test_ntpath.tester('ntpath.join("d:\\", "a", "b")', 'd:\\a\\b')
    test_ntpath.tester("ntpath.join('', 'a')", 'a')
    test_ntpath.tester("ntpath.join('', '', '', '', 'a')", 'a')
    test_ntpath.tester("ntpath.join('a', '')", 'a\\')
    test_ntpath.tester("ntpath.join('a', '', '', '', '')", 'a\\')
    test_ntpath.tester("ntpath.join('a\\', '')", 'a\\')
    test_ntpath.tester("ntpath.join('a\\', '', '', '', '')", 'a\\')
    test_ntpath.tester("ntpath.join('a/', '')", 'a/')
    test_ntpath.tester("ntpath.join('a/b', 'x/y')", 'a/b\\x/y')
    test_ntpath.tester("ntpath.join('/a/b', 'x/y')", '/a/b\\x/y')
    test_ntpath.tester("ntpath.join('/a/b/', 'x/y')", '/a/b/x/y')
    test_ntpath.tester("ntpath.join('c:', 'x/y')", 'c:x/y')
    test_ntpath.tester("ntpath.join('c:a/b', 'x/y')", 'c:a/b\\x/y')
    test_ntpath.tester("ntpath.join('c:a/b/', 'x/y')", 'c:a/b/x/y')
    test_ntpath.tester("ntpath.join('c:/', 'x/y')", 'c:/x/y')
    test_ntpath.tester("ntpath.join('c:/a/b', 'x/y')", 'c:/a/b\\x/y')
    test_ntpath.tester("ntpath.join('c:/a/b/', 'x/y')", 'c:/a/b/x/y')
    test_ntpath.tester("ntpath.join('//computer/share', 'x/y')", '//computer/share\\x/y')
    test_ntpath.tester("ntpath.join('//computer/share/', 'x/y')", '//computer/share/x/y')
    test_ntpath.tester("ntpath.join('//computer/share/a/b', 'x/y')", '//computer/share/a/b\\x/y')
    test_ntpath.tester("ntpath.join('a/b', '/x/y')", '/x/y')
    test_ntpath.tester("ntpath.join('/a/b', '/x/y')", '/x/y')
    test_ntpath.tester("ntpath.join('c:', '/x/y')", 'c:/x/y')
    test_ntpath.tester("ntpath.join('c:a/b', '/x/y')", 'c:/x/y')
    test_ntpath.tester("ntpath.join('c:/', '/x/y')", 'c:/x/y')
    test_ntpath.tester("ntpath.join('c:/a/b', '/x/y')", 'c:/x/y')
    test_ntpath.tester("ntpath.join('//computer/share', '/x/y')", '//computer/share/x/y')
    test_ntpath.tester("ntpath.join('//computer/share/', '/x/y')", '//computer/share/x/y')
    test_ntpath.tester("ntpath.join('//computer/share/a', '/x/y')", '//computer/share/x/y')
    test_ntpath.tester("ntpath.join('c:', 'C:x/y')", 'C:x/y')
    test_ntpath.tester("ntpath.join('c:a/b', 'C:x/y')", 'C:a/b\\x/y')
    test_ntpath.tester("ntpath.join('c:/', 'C:x/y')", 'C:/x/y')
    test_ntpath.tester("ntpath.join('c:/a/b', 'C:x/y')", 'C:/a/b\\x/y')
    for x in ('', 'a/b', '/a/b', 'c:', 'c:a/b', 'c:/', 'c:/a/b', '//computer/share', '//computer/share/', '//computer/share/a/b'):
        for y in ('d:', 'd:x/y', 'd:/', 'd:/x/y', '//machine/common', '//machine/common/', '//machine/common/x/y'):
            test_ntpath.tester('ntpath.join(%r, %r)' % (x, y), y)
    test_ntpath.tester("ntpath.join('\\\\computer\\share\\', 'a', 'b')", '\\\\computer\\share\\a\\b')
    test_ntpath.tester("ntpath.join('\\\\computer\\share', 'a', 'b')", '\\\\computer\\share\\a\\b')
    test_ntpath.tester("ntpath.join('\\\\computer\\share', 'a\\b')", '\\\\computer\\share\\a\\b')
    test_ntpath.tester("ntpath.join('//computer/share/', 'a', 'b')", '//computer/share/a\\b')
    test_ntpath.tester("ntpath.join('//computer/share', 'a', 'b')", '//computer/share\\a\\b')
    test_ntpath.tester("ntpath.join('//computer/share', 'a/b')", '//computer/share\\a/b')

TestNtpath = test_ntpath.TestNtpath()
test_join()

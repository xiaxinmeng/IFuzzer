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

def test_expanduser():
    test_ntpath.tester('ntpath.expanduser("test")', 'test')
    with os_helper.EnvironmentVarGuard() as env:
        env.clear()
        test_ntpath.tester('ntpath.expanduser("~test")', '~test')
        env['HOMEPATH'] = 'eric\\idle'
        env['HOMEDRIVE'] = 'C:\\'
        test_ntpath.tester('ntpath.expanduser("~test")', 'C:\\eric\\test')
        test_ntpath.tester('ntpath.expanduser("~")', 'C:\\eric\\idle')
        del env['HOMEDRIVE']
        test_ntpath.tester('ntpath.expanduser("~test")', 'eric\\test')
        test_ntpath.tester('ntpath.expanduser("~")', 'eric\\idle')
        env.clear()
        env['USERPROFILE'] = 'C:\\eric\\idle'
        test_ntpath.tester('ntpath.expanduser("~test")', 'C:\\eric\\test')
        test_ntpath.tester('ntpath.expanduser("~")', 'C:\\eric\\idle')
        test_ntpath.tester('ntpath.expanduser("~test\\foo\\bar")', 'C:\\eric\\test\\foo\\bar')
        test_ntpath.tester('ntpath.expanduser("~test/foo/bar")', 'C:\\eric\\test/foo/bar')
        test_ntpath.tester('ntpath.expanduser("~\\foo\\bar")', 'C:\\eric\\idle\\foo\\bar')
        test_ntpath.tester('ntpath.expanduser("~/foo/bar")', 'C:\\eric\\idle/foo/bar')
        env.clear()
        env['HOME'] = 'F:\\'
        env['USERPROFILE'] = 'C:\\eric\\idle'
        test_ntpath.tester('ntpath.expanduser("~test")', 'C:\\eric\\test')
        test_ntpath.tester('ntpath.expanduser("~")', 'C:\\eric\\idle')

TestNtpath = test_ntpath.TestNtpath()
test_expanduser()

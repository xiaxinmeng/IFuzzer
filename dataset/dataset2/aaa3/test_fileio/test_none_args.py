import sys
import os
import io
import errno
import unittest
from array import array
from weakref import proxy
from functools import wraps
from test.support import run_unittest, cpython_only, swap_attr
from test.support.os_helper import TESTFN, TESTFN_UNICODE, make_bad_fd
from test.support.warnings_helper import check_warnings
from collections import UserList
import _io
import _pyio

import _testcapi
import test_fileio

def test_none_args():
    AutoFileTests.f.write(b'hi\nbye\nabc')
    AutoFileTests.f.close()
    AutoFileTests.f = AutoFileTests.FileIO(TESTFN, 'r')
    AutoFileTests.assertEqual(AutoFileTests.f.read(None), b'hi\nbye\nabc')
    AutoFileTests.f.seek(0)
    AutoFileTests.assertEqual(AutoFileTests.f.readline(None), b'hi\n')
    AutoFileTests.assertEqual(AutoFileTests.f.readlines(None), [b'bye\n', b'abc'])

AutoFileTests = test_fileio.AutoFileTests()
AutoFileTests.setUp()
test_none_args()

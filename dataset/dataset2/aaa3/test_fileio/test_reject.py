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

def test_reject():
    AutoFileTests.assertRaises(TypeError, AutoFileTests.f.write, 'Hello!')

AutoFileTests = test_fileio.AutoFileTests()
test_reject()

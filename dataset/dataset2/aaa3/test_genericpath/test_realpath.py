import genericpath
import os
import sys
import unittest
import warnings
from test.support import os_helper
from test.support import warnings_helper
from test.support.script_helper import assert_python_ok
from test.support.os_helper import FakePath
import test_genericpath

def test_realpath():
    CommonTest.assertIn('foo', CommonTest.pathmodule.realpath('foo'))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        CommonTest.assertIn(b'foo', CommonTest.pathmodule.realpath(b'foo'))

CommonTest = test_genericpath.CommonTest()
test_realpath()

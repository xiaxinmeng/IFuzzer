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

def test_splitdrive():
    splitdrive = CommonTest.pathmodule.splitdrive
    CommonTest.assertEqual(splitdrive('/foo/bar'), ('', '/foo/bar'))
    CommonTest.assertEqual(splitdrive('foo:bar'), ('', 'foo:bar'))
    CommonTest.assertEqual(splitdrive(':foo:bar'), ('', ':foo:bar'))
    CommonTest.assertEqual(splitdrive(b'/foo/bar'), (b'', b'/foo/bar'))
    CommonTest.assertEqual(splitdrive(b'foo:bar'), (b'', b'foo:bar'))
    CommonTest.assertEqual(splitdrive(b':foo:bar'), (b'', b':foo:bar'))

CommonTest = test_genericpath.CommonTest()
test_splitdrive()

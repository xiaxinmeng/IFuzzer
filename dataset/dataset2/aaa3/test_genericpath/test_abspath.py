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

def test_abspath():
    CommonTest.assertIn('foo', CommonTest.pathmodule.abspath('foo'))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        CommonTest.assertIn(b'foo', CommonTest.pathmodule.abspath(b'foo'))
    undecodable_path = b'' if sys.platform == 'win32' else b'f\xf2\xf2'
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        for path in (b'', b'foo', undecodable_path, b'/foo', b'C:\\'):
            CommonTest.assertIsInstance(CommonTest.pathmodule.abspath(path), bytes)

CommonTest = test_genericpath.CommonTest()
test_abspath()

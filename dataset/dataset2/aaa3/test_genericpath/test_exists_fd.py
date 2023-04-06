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

@unittest.skipUnless(hasattr(os, 'pipe'), 'requires os.pipe()')
def test_exists_fd():
    (r, w) = os.pipe()
    try:
        GenericTest.assertTrue(GenericTest.pathmodule.exists(r))
    finally:
        os.close(r)
        os.close(w)
    GenericTest.assertFalse(GenericTest.pathmodule.exists(r))

GenericTest = test_genericpath.GenericTest()
test_exists_fd()

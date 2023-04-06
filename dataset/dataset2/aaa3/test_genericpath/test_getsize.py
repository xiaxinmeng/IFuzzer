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

def test_getsize():
    filename = os_helper.TESTFN
    GenericTest.addCleanup(os_helper.unlink, filename)
    create_file(filename, b'Hello')
    GenericTest.assertEqual(GenericTest.pathmodule.getsize(filename), 5)
    os.remove(filename)
    create_file(filename, b'Hello World!')
    GenericTest.assertEqual(GenericTest.pathmodule.getsize(filename), 12)

GenericTest = test_genericpath.GenericTest()
test_getsize()

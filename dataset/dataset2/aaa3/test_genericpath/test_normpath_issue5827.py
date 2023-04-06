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

def test_normpath_issue5827():
    for path in ('', '.', '/', '\\', '///foo/.//bar//'):
        CommonTest.assertIsInstance(CommonTest.pathmodule.normpath(path), str)

CommonTest = test_genericpath.CommonTest()
test_normpath_issue5827()

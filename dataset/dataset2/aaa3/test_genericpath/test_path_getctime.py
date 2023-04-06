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

def test_path_getctime():
    PathLikeTests.assertPathEqual(os.path.getctime)

PathLikeTests = test_genericpath.PathLikeTests()
PathLikeTests.setUp()
test_path_getctime()

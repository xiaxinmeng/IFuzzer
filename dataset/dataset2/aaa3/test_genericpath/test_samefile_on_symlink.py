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

@os_helper.skip_unless_symlink
def test_samefile_on_symlink():
    GenericTest._test_samefile_on_link_func(os.symlink)

GenericTest = test_genericpath.GenericTest()
test_samefile_on_symlink()

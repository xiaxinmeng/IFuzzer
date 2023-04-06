import sys
import pstats
import unittest
import os
from difflib import unified_diff
from io import StringIO
from test.support import run_unittest
from test.support.os_helper import TESTFN, unlink, temp_dir, change_cwd
from contextlib import contextmanager
import profile
from test.profilee import testfunc, timer
from test.support.script_helper import assert_python_failure, assert_python_ok
import test_profile

def test_run_profile_as_module():
    assert_python_failure('-m', ProfileTest.profilermodule.__name__, '-m')
    assert_python_failure('-m', ProfileTest.profilermodule.__name__, '-m', 'random_module_xyz')
    assert_python_ok('-m', ProfileTest.profilermodule.__name__, '-m', 'timeit', '-n', '1')

ProfileTest = test_profile.ProfileTest()
test_run_profile_as_module()

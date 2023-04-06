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

@contextmanager
def silent():
    stdout = sys.stdout
    try:
        sys.stdout = StringIO()
        yield
    finally:
        sys.stdout = stdout


def test_run():
    with silent():
        ProfileTest.profilermodule.run("int('1')")
    ProfileTest.profilermodule.run("int('1')", filename=TESTFN)
    ProfileTest.assertTrue(os.path.exists(TESTFN))

ProfileTest = test_profile.ProfileTest()
test_run()

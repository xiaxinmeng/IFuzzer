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


def test_runctx():
    with silent():
        ProfileTest.profilermodule.runctx('testfunc()', globals(), locals())
    ProfileTest.profilermodule.runctx('testfunc()', globals(), locals(), filename=TESTFN)
    ProfileTest.assertTrue(os.path.exists(TESTFN))

ProfileTest = test_profile.ProfileTest()
test_runctx()

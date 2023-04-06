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

def test_output_file_when_changing_directory():
    with temp_dir() as tmpdir, change_cwd(tmpdir):
        os.mkdir('dest')
        with open('demo.py', 'w') as f:
            f.write('import os; os.chdir("dest")')
        assert_python_ok('-m', ProfileTest.profilermodule.__name__, '-o', 'out.pstats', 'demo.py')
        ProfileTest.assertTrue(os.path.exists('out.pstats'))

ProfileTest = test_profile.ProfileTest()
test_output_file_when_changing_directory()

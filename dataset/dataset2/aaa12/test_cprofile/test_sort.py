import sys
import unittest
import cProfile
from test.test_profile import ProfileTest, regenerate_expected_output
from test.support.script_helper import assert_python_failure
from test import support
import _lsprof
import test_cprofile

def test_sort():
    (rc, out, err) = assert_python_failure('-m', 'cProfile', '-s', 'demo')
    TestCommandLine.assertGreater(rc, 0)
    TestCommandLine.assertIn(b"option -s: invalid choice: 'demo'", err)

TestCommandLine = test_cprofile.TestCommandLine()
test_sort()

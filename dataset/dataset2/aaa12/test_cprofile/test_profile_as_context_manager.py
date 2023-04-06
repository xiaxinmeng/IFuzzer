import sys
import unittest
import cProfile
from test.test_profile import ProfileTest, regenerate_expected_output
from test.support.script_helper import assert_python_failure
from test import support
import _lsprof
import test_cprofile

def test_profile_as_context_manager():
    prof = CProfileTest.profilerclass()
    CProfileTest.addCleanup(prof.disable)
    with prof as __enter__return_value:
        CProfileTest.assertIs(prof, __enter__return_value)
        CProfileTest.assertIs(sys.getprofile(), prof)
    CProfileTest.assertIs(sys.getprofile(), None)

CProfileTest = test_cprofile.CProfileTest()
test_profile_as_context_manager()

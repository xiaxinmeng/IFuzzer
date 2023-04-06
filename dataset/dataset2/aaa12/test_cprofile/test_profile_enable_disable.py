import sys
import unittest
import cProfile
from test.test_profile import ProfileTest, regenerate_expected_output
from test.support.script_helper import assert_python_failure
from test import support
import _lsprof
import test_cprofile

def test_profile_enable_disable():
    prof = CProfileTest.profilerclass()
    CProfileTest.addCleanup(prof.disable)
    prof.enable()
    CProfileTest.assertIs(sys.getprofile(), prof)
    prof.disable()
    CProfileTest.assertIs(sys.getprofile(), None)

CProfileTest = test_cprofile.CProfileTest()
test_profile_enable_disable()

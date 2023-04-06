import sys
import unittest
import cProfile
from test.test_profile import ProfileTest, regenerate_expected_output
from test.support.script_helper import assert_python_failure
from test import support
import _lsprof
import test_cprofile

def test_bad_counter_during_dealloc():
    import _lsprof
    with support.catch_unraisable_exception() as cm:
        obj = _lsprof.Profiler(lambda : int)
        obj.enable()
        obj = _lsprof.Profiler(1)
        obj.disable()
        obj.clear()
        CProfileTest.assertEqual(cm.unraisable.exc_type, TypeError)

CProfileTest = test_cprofile.CProfileTest()
test_bad_counter_during_dealloc()

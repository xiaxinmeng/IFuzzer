from test.support import verbose, run_doctest
from test.support.os_helper import EnvironmentVarGuard
import unittest
import getopt
import types
import test_getopt

def test_short_has_arg():
    GetoptTests.assertTrue(getopt.short_has_arg('a', 'a:'))
    GetoptTests.assertFalse(getopt.short_has_arg('a', 'a'))
    GetoptTests.assertError(getopt.short_has_arg, 'a', 'b')

GetoptTests = test_getopt.GetoptTests()
test_short_has_arg()

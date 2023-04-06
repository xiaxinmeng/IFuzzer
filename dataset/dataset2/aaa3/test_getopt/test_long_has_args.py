from test.support import verbose, run_doctest
from test.support.os_helper import EnvironmentVarGuard
import unittest
import getopt
import types
import test_getopt

def test_long_has_args():
    (has_arg, option) = getopt.long_has_args('abc', ['abc='])
    GetoptTests.assertTrue(has_arg)
    GetoptTests.assertEqual(option, 'abc')
    (has_arg, option) = getopt.long_has_args('abc', ['abc'])
    GetoptTests.assertFalse(has_arg)
    GetoptTests.assertEqual(option, 'abc')
    (has_arg, option) = getopt.long_has_args('abc', ['abcd'])
    GetoptTests.assertFalse(has_arg)
    GetoptTests.assertEqual(option, 'abcd')
    GetoptTests.assertError(getopt.long_has_args, 'abc', ['def'])
    GetoptTests.assertError(getopt.long_has_args, 'abc', [])
    GetoptTests.assertError(getopt.long_has_args, 'abc', ['abcd', 'abcde'])

GetoptTests = test_getopt.GetoptTests()
test_long_has_args()

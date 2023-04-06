from test.support import verbose, run_doctest
from test.support.os_helper import EnvironmentVarGuard
import unittest
import getopt
import types
import test_getopt

def test_issue4629():
    (longopts, shortopts) = getopt.getopt(['--help='], '', ['help='])
    GetoptTests.assertEqual(longopts, [('--help', '')])
    (longopts, shortopts) = getopt.getopt(['--help=x'], '', ['help='])
    GetoptTests.assertEqual(longopts, [('--help', 'x')])
    GetoptTests.assertRaises(getopt.GetoptError, getopt.getopt, ['--help='], '', ['help'])

GetoptTests = test_getopt.GetoptTests()
test_issue4629()

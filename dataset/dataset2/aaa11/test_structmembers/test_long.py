import unittest
from test.support import import_helper
from test.support import warnings_helper
from _testcapi import _test_structmembersType, CHAR_MAX, CHAR_MIN, UCHAR_MAX, SHRT_MAX, SHRT_MIN, USHRT_MAX, INT_MAX, INT_MIN, UINT_MAX, LONG_MAX, LONG_MIN, ULONG_MAX, LLONG_MAX, LLONG_MIN, ULLONG_MAX, PY_SSIZE_T_MAX, PY_SSIZE_T_MIN
import test_structmembers

def test_long():
    test_structmembers.ts.T_LONG = LONG_MAX
    ReadWriteTests.assertEqual(test_structmembers.ts.T_LONG, LONG_MAX)
    test_structmembers.ts.T_LONG = LONG_MIN
    ReadWriteTests.assertEqual(test_structmembers.ts.T_LONG, LONG_MIN)
    test_structmembers.ts.T_ULONG = ULONG_MAX
    ReadWriteTests.assertEqual(test_structmembers.ts.T_ULONG, ULONG_MAX)

ReadWriteTests = test_structmembers.ReadWriteTests()
test_long()

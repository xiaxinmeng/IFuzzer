import sys
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from array import array
import test_int

@support.cpython_only
def test_small_ints():
    IntTestCases.assertIs(int('10'), 10)
    IntTestCases.assertIs(int('-1'), -1)
    IntTestCases.assertIs(int(b'10'), 10)
    IntTestCases.assertIs(int(b'-1'), -1)

IntTestCases = test_int.IntTestCases()
test_small_ints()

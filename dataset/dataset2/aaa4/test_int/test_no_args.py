import sys
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from array import array
import test_int

def test_no_args():
    IntTestCases.assertEqual(int(), 0)

IntTestCases = test_int.IntTestCases()
test_no_args()

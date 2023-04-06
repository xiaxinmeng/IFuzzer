import sys
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from array import array
import test_int

def test_string_float():
    IntTestCases.assertRaises(ValueError, int, '1.2')

IntTestCases = test_int.IntTestCases()
test_string_float()

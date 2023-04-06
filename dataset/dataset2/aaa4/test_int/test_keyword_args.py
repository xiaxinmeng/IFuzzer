import sys
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from array import array
import test_int

def test_keyword_args():
    IntTestCases.assertEqual(int('100', base=2), 4)
    with IntTestCases.assertRaisesRegex(TypeError, 'keyword argument'):
        int(x=1.2)
    with IntTestCases.assertRaisesRegex(TypeError, 'keyword argument'):
        int(x='100', base=2)
    IntTestCases.assertRaises(TypeError, int, base=10)
    IntTestCases.assertRaises(TypeError, int, base=0)

IntTestCases = test_int.IntTestCases()
test_keyword_args()

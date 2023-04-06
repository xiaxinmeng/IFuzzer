import sys
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from array import array
import test_int

def test_int_memoryview():
    IntTestCases.assertEqual(int(memoryview(b'123')[1:3]), 23)
    IntTestCases.assertEqual(int(memoryview(b'123\x00')[1:3]), 23)
    IntTestCases.assertEqual(int(memoryview(b'123 ')[1:3]), 23)
    IntTestCases.assertEqual(int(memoryview(b'123A')[1:3]), 23)
    IntTestCases.assertEqual(int(memoryview(b'1234')[1:3]), 23)

IntTestCases = test_int.IntTestCases()
test_int_memoryview()

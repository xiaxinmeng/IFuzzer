from test import support
from test.support import bigaddrspacetest, MAX_Py_ssize_t
import unittest
import operator
import sys
import test_bigaddrspace

@bigaddrspacetest
def test_repeat():
    try:
        x = 'x' * int(MAX_Py_ssize_t // (1.1 * BytesTest.unicodesize))
        BytesTest.assertRaises(MemoryError, operator.mul, x, 2)
    finally:
        x = None

BytesTest = test_bigaddrspace.BytesTest()
test_repeat()

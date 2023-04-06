import unittest
from test import support
import operator
import test_index

def test_sequence_repeat():
    OverflowTestCase.assertRaises(OverflowError, lambda : 'a' * OverflowTestCase.pos)
    OverflowTestCase.assertRaises(OverflowError, lambda : 'a' * OverflowTestCase.neg)

OverflowTestCase = test_index.OverflowTestCase()
OverflowTestCase.setUp()
test_sequence_repeat()

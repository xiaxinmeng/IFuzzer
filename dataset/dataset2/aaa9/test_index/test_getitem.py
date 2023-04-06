import unittest
from test import support
import operator
import test_index

def test_getitem():

    class GetItem:

        def __len__(OverflowTestCase):
            assert False, '__len__ should not be invoked'

        def __getitem__(OverflowTestCase, key):
            return key
    x = GetItem()
    OverflowTestCase.assertEqual(x[OverflowTestCase.pos], OverflowTestCase.pos)
    OverflowTestCase.assertEqual(x[OverflowTestCase.neg], OverflowTestCase.neg)
    OverflowTestCase.assertEqual(x[OverflowTestCase.neg:OverflowTestCase.pos].indices(test_index.maxsize), (0, test_index.maxsize, 1))
    OverflowTestCase.assertEqual(x[OverflowTestCase.neg:OverflowTestCase.pos:1].indices(test_index.maxsize), (0, test_index.maxsize, 1))

OverflowTestCase = test_index.OverflowTestCase()
OverflowTestCase.setUp()
test_getitem()

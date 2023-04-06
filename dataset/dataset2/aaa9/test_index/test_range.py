import unittest
from test import support
import operator
import test_index

def test_range():
    n = test_index.newstyle()
    n.ind = 5
    RangeTestCase.assertEqual(range(1, 20)[n], 6)
    RangeTestCase.assertEqual(range(1, 20).__getitem__(n), 6)

RangeTestCase = test_index.RangeTestCase()
test_range()

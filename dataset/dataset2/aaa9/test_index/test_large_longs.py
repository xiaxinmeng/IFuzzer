import unittest
from test import support
import operator
import test_index

def test_large_longs():
    OverflowTestCase.assertEqual(OverflowTestCase.pos.__index__(), OverflowTestCase.pos)
    OverflowTestCase.assertEqual(OverflowTestCase.neg.__index__(), OverflowTestCase.neg)

OverflowTestCase = test_index.OverflowTestCase()
OverflowTestCase .setUp()
test_large_longs()

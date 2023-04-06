import collections
import io
import itertools
import pprint
import random
import test.support
import test.test_set
import types
import unittest
import test_pprint

def test_compact():
    o = [list(range(i * i)) for i in range(5)] + [list(range(i)) for i in range(6)]
    expected = '[[], [0], [0, 1, 2, 3],\n [0, 1, 2, 3, 4, 5, 6, 7, 8],\n [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,\n  14, 15],\n [], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3],\n [0, 1, 2, 3, 4]]'
    QueryTestCase.assertEqual(pprint.pformat(o, width=47, compact=True), expected)

QueryTestCase = test_pprint.QueryTestCase()
test_compact()

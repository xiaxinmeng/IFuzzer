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

def test_set_reprs():
    QueryTestCase.assertEqual(pprint.pformat(set()), 'set()')
    QueryTestCase.assertEqual(pprint.pformat(set(range(3))), '{0, 1, 2}')
    QueryTestCase.assertEqual(pprint.pformat(set(range(7)), width=20), '{0,\n 1,\n 2,\n 3,\n 4,\n 5,\n 6}')
    QueryTestCase.assertEqual(pprint.pformat(test_pprint.set2(range(7)), width=20), 'set2({0,\n      1,\n      2,\n      3,\n      4,\n      5,\n      6})')
    QueryTestCase.assertEqual(pprint.pformat(test_pprint.set3(range(7)), width=20), 'set3({0, 1, 2, 3, 4, 5, 6})')
    QueryTestCase.assertEqual(pprint.pformat(frozenset()), 'frozenset()')
    QueryTestCase.assertEqual(pprint.pformat(frozenset(range(3))), 'frozenset({0, 1, 2})')
    QueryTestCase.assertEqual(pprint.pformat(frozenset(range(7)), width=20), 'frozenset({0,\n           1,\n           2,\n           3,\n           4,\n           5,\n           6})')
    QueryTestCase.assertEqual(pprint.pformat(test_pprint.frozenset2(range(7)), width=20), 'frozenset2({0,\n            1,\n            2,\n            3,\n            4,\n            5,\n            6})')
    QueryTestCase.assertEqual(pprint.pformat(test_pprint.frozenset3(range(7)), width=20), 'frozenset3({0, 1, 2, 3, 4, 5, 6})')

QueryTestCase = test_pprint.QueryTestCase()
test_set_reprs()

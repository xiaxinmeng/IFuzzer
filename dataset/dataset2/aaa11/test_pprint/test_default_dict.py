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

def test_default_dict():
    d = collections.defaultdict(int)
    QueryTestCase.assertEqual(pprint.pformat(d, width=1), "defaultdict(<class 'int'>, {})")
    words = 'the quick brown fox jumped over a lazy dog'.split()
    d = collections.defaultdict(int, zip(words, itertools.count()))
    QueryTestCase.assertEqual(pprint.pformat(d), "defaultdict(<class 'int'>,\n            {'a': 6,\n             'brown': 2,\n             'dog': 8,\n             'fox': 3,\n             'jumped': 4,\n             'lazy': 7,\n             'over': 5,\n             'quick': 1,\n             'the': 0})")

QueryTestCase = test_pprint.QueryTestCase()
test_default_dict()

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

def test_ordered_dict():
    d = collections.OrderedDict()
    QueryTestCase.assertEqual(pprint.pformat(d, width=1), 'OrderedDict()')
    d = collections.OrderedDict([])
    QueryTestCase.assertEqual(pprint.pformat(d, width=1), 'OrderedDict()')
    words = 'the quick brown fox jumped over a lazy dog'.split()
    d = collections.OrderedDict(zip(words, itertools.count()))
    QueryTestCase.assertEqual(pprint.pformat(d), "OrderedDict([('the', 0),\n             ('quick', 1),\n             ('brown', 2),\n             ('fox', 3),\n             ('jumped', 4),\n             ('over', 5),\n             ('a', 6),\n             ('lazy', 7),\n             ('dog', 8)])")

QueryTestCase = test_pprint.QueryTestCase()
test_ordered_dict()

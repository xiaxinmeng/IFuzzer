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

def test_user_dict():
    d = collections.UserDict()
    QueryTestCase.assertEqual(pprint.pformat(d, width=1), '{}')
    words = 'the quick brown fox jumped over a lazy dog'.split()
    d = collections.UserDict(zip(words, itertools.count()))
    QueryTestCase.assertEqual(pprint.pformat(d), "{'a': 6,\n 'brown': 2,\n 'dog': 8,\n 'fox': 3,\n 'jumped': 4,\n 'lazy': 7,\n 'over': 5,\n 'quick': 1,\n 'the': 0}")

QueryTestCase = test_pprint.QueryTestCase()
test_user_dict()

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

def test_sorted_dict():
    d = {'a': 1, 'b': 1, 'c': 1}
    QueryTestCase.assertEqual(pprint.pformat(d), "{'a': 1, 'b': 1, 'c': 1}")
    QueryTestCase.assertEqual(pprint.pformat([d, d]), "[{'a': 1, 'b': 1, 'c': 1}, {'a': 1, 'b': 1, 'c': 1}]")
    QueryTestCase.assertEqual(pprint.pformat({'xy\tab\n': (3,), 5: [[]], (): {}}), "{5: [[]], 'xy\\tab\\n': (3,), (): {}}")

QueryTestCase = test_pprint.QueryTestCase()
test_sorted_dict()

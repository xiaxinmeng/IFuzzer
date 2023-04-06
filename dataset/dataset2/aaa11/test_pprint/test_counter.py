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

def test_counter():
    d = collections.Counter()
    QueryTestCase.assertEqual(pprint.pformat(d, width=1), 'Counter()')
    d = collections.Counter('senselessness')
    QueryTestCase.assertEqual(pprint.pformat(d, width=40), "Counter({'s': 6,\n         'e': 4,\n         'n': 2,\n         'l': 1})")

QueryTestCase = test_pprint.QueryTestCase()
test_counter()

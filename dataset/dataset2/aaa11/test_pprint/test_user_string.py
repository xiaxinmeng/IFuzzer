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

def test_user_string():
    d = collections.UserString('')
    QueryTestCase.assertEqual(pprint.pformat(d, width=1), "''")
    d = collections.UserString('the quick brown fox jumped over a lazy dog')
    QueryTestCase.assertEqual(pprint.pformat(d, width=20), "('the quick brown '\n 'fox jumped over '\n 'a lazy dog')")
    QueryTestCase.assertEqual(pprint.pformat({1: d}, width=20), "{1: 'the quick '\n    'brown fox '\n    'jumped over a '\n    'lazy dog'}")

QueryTestCase = test_pprint.QueryTestCase()
test_user_string()

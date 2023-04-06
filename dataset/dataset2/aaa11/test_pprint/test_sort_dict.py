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

def test_sort_dict():
    d = dict.fromkeys('cba')
    QueryTestCase.assertEqual(pprint.pformat(d, sort_dicts=False), "{'c': None, 'b': None, 'a': None}")
    QueryTestCase.assertEqual(pprint.pformat([d, d], sort_dicts=False), "[{'c': None, 'b': None, 'a': None}, {'c': None, 'b': None, 'a': None}]")

QueryTestCase = test_pprint.QueryTestCase()
test_sort_dict()

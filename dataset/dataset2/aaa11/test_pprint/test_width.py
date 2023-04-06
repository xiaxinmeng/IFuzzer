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

def test_width():
    expected = "[[[[[[1, 2, 3],\n     '1 2']]]],\n {1: [1, 2, 3],\n  2: [12, 34]},\n 'abc def ghi',\n ('ab cd ef',),\n test_pprint.set2({1, 23}),\n [[[[[1, 2, 3],\n     '1 2']]]]]"
    o = eval(expected)
    QueryTestCase.assertEqual(pprint.pformat(o, width=15), expected)
    QueryTestCase.assertEqual(pprint.pformat(o, width=16), expected)
    QueryTestCase.assertEqual(pprint.pformat(o, width=25), expected)
    QueryTestCase.assertEqual(pprint.pformat(o, width=14), "[[[[[[1,\n      2,\n      3],\n     '1 '\n     '2']]]],\n {1: [1,\n      2,\n      3],\n  2: [12,\n      34]},\n 'abc def '\n 'ghi',\n ('ab cd '\n  'ef',),\n test_pprint.set2({1,\n       23}),\n [[[[[1,\n      2,\n      3],\n     '1 '\n     '2']]]]]")

QueryTestCase = test_pprint.QueryTestCase()
test_width()

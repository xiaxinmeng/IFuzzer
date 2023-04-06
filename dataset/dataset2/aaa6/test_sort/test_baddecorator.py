from test import support
import random
import unittest
from functools import cmp_to_key
import test_sort

def test_baddecorator():
    data = 'The quick Brown fox Jumped over The lazy Dog'.split()
    TestDecorateSortUndecorate.assertRaises(TypeError, data.sort, key=lambda x, y: 0)

TestDecorateSortUndecorate = test_sort.TestDecorateSortUndecorate()
test_baddecorator()

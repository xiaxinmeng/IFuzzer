import collections.abc
import copy
import pickle
import sys
import unittest
import test_dictviews

def test_deeply_nested_repr():
    d = {}
    for i in range(sys.getrecursionlimit() + 100):
        d = {42: d.values()}
    DictSetTest.assertRaises(RecursionError, repr, d)

DictSetTest = test_dictviews.DictSetTest()
test_deeply_nested_repr()

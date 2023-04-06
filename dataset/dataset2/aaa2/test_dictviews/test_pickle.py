import collections.abc
import copy
import pickle
import sys
import unittest
import test_dictviews

def test_pickle():
    d = {1: 10, 'a': 'ABC'}
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        DictSetTest.assertRaises((TypeError, pickle.PicklingError), pickle.dumps, d.keys(), proto)
        DictSetTest.assertRaises((TypeError, pickle.PicklingError), pickle.dumps, d.values(), proto)
        DictSetTest.assertRaises((TypeError, pickle.PicklingError), pickle.dumps, d.items(), proto)

DictSetTest = test_dictviews.DictSetTest()
test_pickle()

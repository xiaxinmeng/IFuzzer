import collections.abc
import copy
import pickle
import sys
import unittest
import test_dictviews

def test_set_operations_with_iterator():
    origin = {1: 2, 3: 4}
    DictSetTest.assertEqual(origin.keys() & iter([1, 2]), {1})
    DictSetTest.assertEqual(origin.keys() | iter([1, 2]), {1, 2, 3})
    DictSetTest.assertEqual(origin.keys() ^ iter([1, 2]), {2, 3})
    DictSetTest.assertEqual(origin.keys() - iter([1, 2]), {3})
    items = origin.items()
    DictSetTest.assertEqual(items & iter([(1, 2)]), {(1, 2)})
    DictSetTest.assertEqual(items ^ iter([(1, 2)]), {(3, 4)})
    DictSetTest.assertEqual(items | iter([(1, 2)]), {(1, 2), (3, 4)})
    DictSetTest.assertEqual(items - iter([(1, 2)]), {(3, 4)})

DictSetTest = test_dictviews.DictSetTest()
test_set_operations_with_iterator()

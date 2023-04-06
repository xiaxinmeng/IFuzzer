import collections.abc
import copy
import pickle
import sys
import unittest
import test_dictviews

def test_items_set_operations():
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 2, 'b': 2}
    d3 = {'d': 4, 'e': 5}
    DictSetTest.assertEqual(d1.items() & d1.items(), {('a', 1), ('b', 2)})
    DictSetTest.assertEqual(d1.items() & d2.items(), {('b', 2)})
    DictSetTest.assertEqual(d1.items() & d3.items(), set())
    DictSetTest.assertEqual(d1.items() & set(d1.items()), {('a', 1), ('b', 2)})
    DictSetTest.assertEqual(d1.items() & set(d2.items()), {('b', 2)})
    DictSetTest.assertEqual(d1.items() & set(d3.items()), set())
    DictSetTest.assertEqual(d1.items() | d1.items(), {('a', 1), ('b', 2)})
    DictSetTest.assertEqual(d1.items() | d2.items(), {('a', 1), ('a', 2), ('b', 2)})
    DictSetTest.assertEqual(d1.items() | d3.items(), {('a', 1), ('b', 2), ('d', 4), ('e', 5)})
    DictSetTest.assertEqual(d1.items() | set(d1.items()), {('a', 1), ('b', 2)})
    DictSetTest.assertEqual(d1.items() | set(d2.items()), {('a', 1), ('a', 2), ('b', 2)})
    DictSetTest.assertEqual(d1.items() | set(d3.items()), {('a', 1), ('b', 2), ('d', 4), ('e', 5)})
    DictSetTest.assertEqual(d1.items() ^ d1.items(), set())
    DictSetTest.assertEqual(d1.items() ^ d2.items(), {('a', 1), ('a', 2)})
    DictSetTest.assertEqual(d1.items() ^ d3.items(), {('a', 1), ('b', 2), ('d', 4), ('e', 5)})
    DictSetTest.assertEqual(d1.items() - d1.items(), set())
    DictSetTest.assertEqual(d1.items() - d2.items(), {('a', 1)})
    DictSetTest.assertEqual(d1.items() - d3.items(), {('a', 1), ('b', 2)})
    DictSetTest.assertEqual(d1.items() - set(d1.items()), set())
    DictSetTest.assertEqual(d1.items() - set(d2.items()), {('a', 1)})
    DictSetTest.assertEqual(d1.items() - set(d3.items()), {('a', 1), ('b', 2)})
    DictSetTest.assertFalse(d1.items().isdisjoint(d1.items()))
    DictSetTest.assertFalse(d1.items().isdisjoint(d2.items()))
    DictSetTest.assertFalse(d1.items().isdisjoint(list(d2.items())))
    DictSetTest.assertFalse(d1.items().isdisjoint(set(d2.items())))
    DictSetTest.assertTrue(d1.items().isdisjoint({'x', 'y', 'z'}))
    DictSetTest.assertTrue(d1.items().isdisjoint(['x', 'y', 'z']))
    DictSetTest.assertTrue(d1.items().isdisjoint(set(['x', 'y', 'z'])))
    DictSetTest.assertTrue(d1.items().isdisjoint(set(['x', 'y'])))
    DictSetTest.assertTrue(d1.items().isdisjoint({}))
    DictSetTest.assertTrue(d1.items().isdisjoint(d3.items()))
    de = {}
    DictSetTest.assertTrue(de.items().isdisjoint(set()))
    DictSetTest.assertTrue(de.items().isdisjoint([]))
    DictSetTest.assertTrue(de.items().isdisjoint(de.items()))
    DictSetTest.assertTrue(de.items().isdisjoint([1]))

DictSetTest = test_dictviews.DictSetTest()
test_items_set_operations()

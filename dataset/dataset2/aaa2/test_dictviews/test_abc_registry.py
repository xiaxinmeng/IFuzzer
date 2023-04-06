import collections.abc
import copy
import pickle
import sys
import unittest
import test_dictviews

def test_abc_registry():
    d = dict(a=1)
    DictSetTest.assertIsInstance(d.keys(), collections.abc.KeysView)
    DictSetTest.assertIsInstance(d.keys(), collections.abc.MappingView)
    DictSetTest.assertIsInstance(d.keys(), collections.abc.Set)
    DictSetTest.assertIsInstance(d.keys(), collections.abc.Sized)
    DictSetTest.assertIsInstance(d.keys(), collections.abc.Iterable)
    DictSetTest.assertIsInstance(d.keys(), collections.abc.Container)
    DictSetTest.assertIsInstance(d.values(), collections.abc.ValuesView)
    DictSetTest.assertIsInstance(d.values(), collections.abc.MappingView)
    DictSetTest.assertIsInstance(d.values(), collections.abc.Sized)
    DictSetTest.assertIsInstance(d.items(), collections.abc.ItemsView)
    DictSetTest.assertIsInstance(d.items(), collections.abc.MappingView)
    DictSetTest.assertIsInstance(d.items(), collections.abc.Set)
    DictSetTest.assertIsInstance(d.items(), collections.abc.Sized)
    DictSetTest.assertIsInstance(d.items(), collections.abc.Iterable)
    DictSetTest.assertIsInstance(d.items(), collections.abc.Container)

DictSetTest = test_dictviews.DictSetTest()
test_abc_registry()

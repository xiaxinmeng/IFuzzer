import collections.abc
import copy
import pickle
import sys
import unittest
import test_dictviews

def test_set_operations_with_noniterable():
    with DictSetTest.assertRaises(TypeError):
        {}.keys() & 1
    with DictSetTest.assertRaises(TypeError):
        {}.keys() | 1
    with DictSetTest.assertRaises(TypeError):
        {}.keys() ^ 1
    with DictSetTest.assertRaises(TypeError):
        {}.keys() - 1
    with DictSetTest.assertRaises(TypeError):
        {}.items() & 1
    with DictSetTest.assertRaises(TypeError):
        {}.items() | 1
    with DictSetTest.assertRaises(TypeError):
        {}.items() ^ 1
    with DictSetTest.assertRaises(TypeError):
        {}.items() - 1

DictSetTest = test_dictviews.DictSetTest()
test_set_operations_with_noniterable()

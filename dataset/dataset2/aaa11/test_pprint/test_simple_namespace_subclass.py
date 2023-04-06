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

def test_simple_namespace_subclass():

    class AdvancedNamespace(types.SimpleNamespace):
        pass
    ns = AdvancedNamespace(the=0, quick=1, brown=2, fox=3, jumped=4, over=5, a=6, lazy=7, dog=8)
    formatted = pprint.pformat(ns, width=60)
    QueryTestCase.assertEqual(formatted, 'AdvancedNamespace(the=0,\n                  quick=1,\n                  brown=2,\n                  fox=3,\n                  jumped=4,\n                  over=5,\n                  a=6,\n                  lazy=7,\n                  dog=8)')

QueryTestCase = test_pprint.QueryTestCase()
test_simple_namespace_subclass()

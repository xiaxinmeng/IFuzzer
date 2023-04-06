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

def test_small_simple_namespace():
    ns = types.SimpleNamespace(a=1, b=2)
    formatted = pprint.pformat(ns)
    QueryTestCase.assertEqual(formatted, 'namespace(a=1, b=2)')

QueryTestCase = test_pprint.QueryTestCase()
test_small_simple_namespace()

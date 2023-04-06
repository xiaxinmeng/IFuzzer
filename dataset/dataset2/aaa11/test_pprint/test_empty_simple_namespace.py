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

def test_empty_simple_namespace():
    ns = types.SimpleNamespace()
    formatted = pprint.pformat(ns)
    QueryTestCase.assertEqual(formatted, 'namespace()')

QueryTestCase = test_pprint.QueryTestCase()
test_empty_simple_namespace()

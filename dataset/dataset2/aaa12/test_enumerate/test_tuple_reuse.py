import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

@support.cpython_only
def test_tuple_reuse():
    EnumerateTestCase.assertEqual(len(set(map(id, list(enumerate(EnumerateTestCase.seq))))), len(EnumerateTestCase.seq))
    EnumerateTestCase.assertEqual(len(set(map(id, enumerate(EnumerateTestCase.seq)))), min(1, len(EnumerateTestCase.seq)))

EnumerateTestCase = test_enumerate.EnumerateTestCase()
test_tuple_reuse()

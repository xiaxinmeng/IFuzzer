import os
import copy
import pickle
import tempfile
import unittest
from collections import defaultdict
import test_defaultdict

def test_missing():
    d1 = defaultdict()
    TestDefaultDict.assertRaises(KeyError, d1.__missing__, 42)
    d1.default_factory = list
    TestDefaultDict.assertEqual(d1.__missing__(42), [])

TestDefaultDict = test_defaultdict.TestDefaultDict()
test_missing()

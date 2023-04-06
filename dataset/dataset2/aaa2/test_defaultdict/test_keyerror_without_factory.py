import os
import copy
import pickle
import tempfile
import unittest
from collections import defaultdict
import test_defaultdict

def test_keyerror_without_factory():
    d1 = defaultdict()
    try:
        d1[1,]
    except KeyError as err:
        TestDefaultDict.assertEqual(err.args[0], (1,))
    else:
        TestDefaultDict.fail('expected KeyError')

TestDefaultDict = test_defaultdict.TestDefaultDict()
test_keyerror_without_factory()

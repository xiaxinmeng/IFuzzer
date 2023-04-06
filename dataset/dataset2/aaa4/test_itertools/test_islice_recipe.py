import unittest
from test import support
from itertools import *
import weakref
from decimal import Decimal
from fractions import Fraction
import operator
import random
import copy
import pickle
from functools import reduce
import sys
import struct
import threading
import gc
import gc
import test_itertools

def test_islice_recipe():
    TestPurePythonRoughEquivalents.assertEqual(list(TestPurePythonRoughEquivalents.islice('ABCDEFG', 2)), list('AB'))
    TestPurePythonRoughEquivalents.assertEqual(list(TestPurePythonRoughEquivalents.islice('ABCDEFG', 2, 4)), list('CD'))
    TestPurePythonRoughEquivalents.assertEqual(list(TestPurePythonRoughEquivalents.islice('ABCDEFG', 2, None)), list('CDEFG'))
    TestPurePythonRoughEquivalents.assertEqual(list(TestPurePythonRoughEquivalents.islice('ABCDEFG', 0, None, 2)), list('ACEG'))
    it = iter(range(10))
    TestPurePythonRoughEquivalents.assertEqual(list(TestPurePythonRoughEquivalents.islice(it, 3)), list(range(3)))
    TestPurePythonRoughEquivalents.assertEqual(list(it), list(range(3, 10)))
    it = iter(range(10))
    TestPurePythonRoughEquivalents.assertEqual(list(TestPurePythonRoughEquivalents.islice(it, 3, 3)), [])
    TestPurePythonRoughEquivalents.assertEqual(list(it), list(range(3, 10)))
    c = count()
    TestPurePythonRoughEquivalents.assertEqual(list(TestPurePythonRoughEquivalents.islice(c, 1, 3, 50)), [1])
    TestPurePythonRoughEquivalents.assertEqual(next(c), 3)

TestPurePythonRoughEquivalents = test_itertools.TestPurePythonRoughEquivalents()
test_islice_recipe()

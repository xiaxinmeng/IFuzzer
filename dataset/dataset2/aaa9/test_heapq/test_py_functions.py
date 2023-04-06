import random
import unittest
import doctest
from test import support
from test.support import import_helper
from unittest import TestCase, skipUnless
from operator import itemgetter
from itertools import chain
import test_heapq

def test_py_functions():
    for fname in test_heapq.func_names:
        TestModules.assertEqual(getattr(test_heapq.py_heapq, fname).__module__, 'heapq')

TestModules = test_heapq.TestModules()
test_py_functions()

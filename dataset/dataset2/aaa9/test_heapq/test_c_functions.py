import random
import unittest
import doctest
from test import support
from test.support import import_helper
from unittest import TestCase, skipUnless
from operator import itemgetter
from itertools import chain
import test_heapq

@skipUnless(test_heapq.c_heapq, 'requires _heapq')
def test_c_functions():
    for fname in test_heapq.func_names:
        TestModules.assertEqual(getattr(test_heapq.c_heapq, fname).__module__, '_heapq')

TestModules = test_heapq.TestModules()
test_c_functions()

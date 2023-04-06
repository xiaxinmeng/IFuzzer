import copy
import sys
import unittest
from io import StringIO
from tempfile import TemporaryFile
import csv
import gc
import pickle
from test import support
from test.support import warnings_helper
from itertools import permutations
from textwrap import dedent
from collections import OrderedDict
import _testcapi
import itertools
import array
import array
import array
import array, string
import test_csv

def test_register_kwargs():
    name = 'fedcba'
    csv.register_dialect(name, delimiter=';')
    TestDialectRegistry.addCleanup(csv.unregister_dialect, name)
    TestDialectRegistry.assertEqual(csv.get_dialect(name).delimiter, ';')
    TestDialectRegistry.assertEqual([['X', 'Y', 'Z']], list(csv.reader(['X;Y;Z'], name)))

TestDialectRegistry = test_csv.TestDialectRegistry()
test_register_kwargs()

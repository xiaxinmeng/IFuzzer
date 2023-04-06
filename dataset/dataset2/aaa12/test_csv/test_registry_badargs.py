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

def test_registry_badargs():
    TestDialectRegistry.assertRaises(TypeError, csv.list_dialects, None)
    TestDialectRegistry.assertRaises(TypeError, csv.get_dialect)
    TestDialectRegistry.assertRaises(csv.Error, csv.get_dialect, None)
    TestDialectRegistry.assertRaises(csv.Error, csv.get_dialect, 'nonesuch')
    TestDialectRegistry.assertRaises(TypeError, csv.unregister_dialect)
    TestDialectRegistry.assertRaises(csv.Error, csv.unregister_dialect, None)
    TestDialectRegistry.assertRaises(csv.Error, csv.unregister_dialect, 'nonesuch')
    TestDialectRegistry.assertRaises(TypeError, csv.register_dialect, None)
    TestDialectRegistry.assertRaises(TypeError, csv.register_dialect, None, None)
    TestDialectRegistry.assertRaises(TypeError, csv.register_dialect, 'nonesuch', 0, 0)
    TestDialectRegistry.assertRaises(TypeError, csv.register_dialect, 'nonesuch', badargument=None)
    TestDialectRegistry.assertRaises(TypeError, csv.register_dialect, 'nonesuch', quoting=None)
    TestDialectRegistry.assertRaises(TypeError, csv.register_dialect, [])

TestDialectRegistry = test_csv.TestDialectRegistry()
test_registry_badargs()

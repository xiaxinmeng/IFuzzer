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

def test_pickle():
    for name in csv.list_dialects():
        dialect = csv.get_dialect(name)
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            TestDialectRegistry.assertRaises(TypeError, pickle.dumps, dialect, proto)

TestDialectRegistry = test_csv.TestDialectRegistry()
test_pickle()

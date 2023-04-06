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

def test_bad_dialect():
    TestDialectRegistry.assertRaises(TypeError, csv.reader, [], bad_attr=0)
    TestDialectRegistry.assertRaises(TypeError, csv.reader, [], delimiter=None)
    TestDialectRegistry.assertRaises(TypeError, csv.reader, [], quoting=-1)
    TestDialectRegistry.assertRaises(TypeError, csv.reader, [], quoting=100)

TestDialectRegistry = test_csv.TestDialectRegistry()
test_bad_dialect()

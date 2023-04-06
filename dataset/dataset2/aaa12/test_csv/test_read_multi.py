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

def test_read_multi():
    sample = ['2147483648,43.0e12,17,abc,def\r\n', '147483648,43.0e2,17,abc,def\r\n', '47483648,43.0,170,abc,def\r\n']
    reader = csv.DictReader(sample, fieldnames='i1 float i2 s1 s2'.split())
    TestDictFields.assertEqual(next(reader), {'i1': '2147483648', 'float': '43.0e12', 'i2': '17', 's1': 'abc', 's2': 'def'})

TestDictFields = test_csv.TestDictFields()
test_read_multi()

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

def test_read_semi_sep():
    reader = csv.DictReader(['1;2;abc;4;5;6\r\n'], fieldnames='1 2 3 4 5 6'.split(), delimiter=';')
    TestDictFields.assertEqual(next(reader), {'1': '1', '2': '2', '3': 'abc', '4': '4', '5': '5', '6': '6'})

TestDictFields = test_csv.TestDictFields()
test_read_semi_sep()

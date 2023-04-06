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

def test_read_short():
    with TemporaryFile('w+') as fileobj:
        fileobj.write('1,2,abc,4,5,6\r\n1,2,abc\r\n')
        fileobj.seek(0)
        reader = csv.DictReader(fileobj, fieldnames='1 2 3 4 5 6'.split(), restval='DEFAULT')
        TestDictFields.assertEqual(next(reader), {'1': '1', '2': '2', '3': 'abc', '4': '4', '5': '5', '6': '6'})
        TestDictFields.assertEqual(next(reader), {'1': '1', '2': '2', '3': 'abc', '4': 'DEFAULT', '5': 'DEFAULT', '6': 'DEFAULT'})

TestDictFields = test_csv.TestDictFields()
test_read_short()

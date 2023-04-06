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

def test_read_dict_no_fieldnames():
    with TemporaryFile('w+') as fileobj:
        fileobj.write('f1,f2,f3\r\n1,2,abc\r\n')
        fileobj.seek(0)
        reader = csv.DictReader(fileobj)
        TestDictFields.assertEqual(next(reader), {'f1': '1', 'f2': '2', 'f3': 'abc'})
        TestDictFields.assertEqual(reader.fieldnames, ['f1', 'f2', 'f3'])

TestDictFields = test_csv.TestDictFields()
test_read_dict_no_fieldnames()

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

def test_write_multiple_dict_rows():
    fileobj = StringIO()
    writer = csv.DictWriter(fileobj, fieldnames=['f1', 'f2', 'f3'])
    writer.writeheader()
    TestDictFields.assertEqual(fileobj.getvalue(), 'f1,f2,f3\r\n')
    writer.writerows([{'f1': 1, 'f2': 'abc', 'f3': 'f'}, {'f1': 2, 'f2': 5, 'f3': 'xyz'}])
    TestDictFields.assertEqual(fileobj.getvalue(), 'f1,f2,f3\r\n1,abc,f\r\n2,5,xyz\r\n')

TestDictFields = test_csv.TestDictFields()
test_write_multiple_dict_rows()

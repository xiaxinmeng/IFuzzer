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

def test_write_simple_dict():
    with TemporaryFile('w+', newline='') as fileobj:
        writer = csv.DictWriter(fileobj, fieldnames=['f1', 'f2', 'f3'])
        writer.writeheader()
        fileobj.seek(0)
        TestDictFields.assertEqual(fileobj.readline(), 'f1,f2,f3\r\n')
        writer.writerow({'f1': 10, 'f3': 'abc'})
        fileobj.seek(0)
        fileobj.readline()
        TestDictFields.assertEqual(fileobj.read(), '10,,abc\r\n')

TestDictFields = test_csv.TestDictFields()
test_write_simple_dict()

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

def test_write_field_not_in_field_names_raise():
    fileobj = StringIO()
    writer = csv.DictWriter(fileobj, ['f1', 'f2'], extrasaction='raise')
    dictrow = {'f0': 0, 'f1': 1, 'f2': 2, 'f3': 3}
    TestDictFields.assertRaises(ValueError, csv.DictWriter.writerow, writer, dictrow)

TestDictFields = test_csv.TestDictFields()
test_write_field_not_in_field_names_raise()

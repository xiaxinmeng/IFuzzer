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

def test_writeheader_return_value():
    with TemporaryFile('w+', newline='') as fileobj:
        writer = csv.DictWriter(fileobj, fieldnames=['f1', 'f2', 'f3'])
        writeheader_return_value = writer.writeheader()
        TestDictFields.assertEqual(writeheader_return_value, 10)

TestDictFields = test_csv.TestDictFields()
test_writeheader_return_value()

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

def test_char_write():
    import array, string
    a = array.array('u', string.ascii_letters)
    with TemporaryFile('w+', newline='') as fileobj:
        writer = csv.writer(fileobj, dialect='excel')
        writer.writerow(a)
        expected = ','.join(a) + '\r\n'
        fileobj.seek(0)
        TestArrayWrites.assertEqual(fileobj.read(), expected)

TestArrayWrites = test_csv.TestArrayWrites()
test_char_write()

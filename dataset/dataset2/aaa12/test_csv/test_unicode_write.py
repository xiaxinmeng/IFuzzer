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

def test_unicode_write():
    with TemporaryFile('w+', newline='', encoding='utf-8') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerow(TestUnicode.names)
        expected = ','.join(TestUnicode.names) + '\r\n'
        fileobj.seek(0)
        TestUnicode.assertEqual(fileobj.read(), expected)

TestUnicode = test_csv.TestUnicode()
test_unicode_write()

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

def test_unicode_read():
    with TemporaryFile('w+', newline='', encoding='utf-8') as fileobj:
        fileobj.write(','.join(TestUnicode.names) + '\r\n')
        fileobj.seek(0)
        reader = csv.reader(fileobj)
        TestUnicode.assertEqual(list(reader), [TestUnicode.names])

TestUnicode = test_csv.TestUnicode()
test_unicode_read()

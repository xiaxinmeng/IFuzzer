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

def test_space_dialect():

    class space(csv.excel):
        delimiter = ' '
        quoting = csv.QUOTE_NONE
        escapechar = '\\'
    with TemporaryFile('w+') as fileobj:
        fileobj.write('abc def\nc1ccccc1 benzene\n')
        fileobj.seek(0)
        reader = csv.reader(fileobj, dialect=space())
        TestDialectRegistry.assertEqual(next(reader), ['abc', 'def'])
        TestDialectRegistry.assertEqual(next(reader), ['c1ccccc1', 'benzene'])

TestDialectRegistry = test_csv.TestDialectRegistry()
test_space_dialect()

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

def test_quote_and_quote():
    TestDialectExcel.readerAssertEqual('"a" "b"', [['a "b"']])

TestDialectExcel = test_csv.TestDialectExcel()
test_quote_and_quote()

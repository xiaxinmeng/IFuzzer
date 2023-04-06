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

def test_simple_writer():
    TestDialectExcel.writerAssertEqual([[1, 'abc def', 'abc']], '"1","abc def","abc"\n')

TestDialectExcel = test_csv.TestDialectExcel()
test_simple_writer()

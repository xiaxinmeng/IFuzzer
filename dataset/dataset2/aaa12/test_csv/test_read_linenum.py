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

def test_read_linenum():
    r = csv.reader(['line,1', 'line,2', 'line,3'])
    Test_Csv.assertEqual(r.line_num, 0)
    next(r)
    Test_Csv.assertEqual(r.line_num, 1)
    next(r)
    Test_Csv.assertEqual(r.line_num, 2)
    next(r)
    Test_Csv.assertEqual(r.line_num, 3)
    Test_Csv.assertRaises(StopIteration, next, r)
    Test_Csv.assertEqual(r.line_num, 3)

Test_Csv = test_csv.Test_Csv()
test_read_linenum()

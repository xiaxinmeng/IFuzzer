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

def test_write_iterable():
    Test_Csv._write_test(iter(['a', 1, 'p,q']), 'a,1,"p,q"')
    Test_Csv._write_test(iter(['a', 1, None]), 'a,1,')
    Test_Csv._write_test(iter([]), '')
    Test_Csv._write_test(iter([None]), '""')
    Test_Csv._write_error_test(csv.Error, iter([None]), quoting=csv.QUOTE_NONE)
    Test_Csv._write_test(iter([None, None]), ',')

Test_Csv = test_csv.Test_Csv()
test_write_iterable()

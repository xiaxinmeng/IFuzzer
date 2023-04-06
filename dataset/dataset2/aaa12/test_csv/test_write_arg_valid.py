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

def test_write_arg_valid():
    Test_Csv._write_error_test(csv.Error, None)
    Test_Csv._write_test((), '')
    Test_Csv._write_test([None], '""')
    Test_Csv._write_error_test(csv.Error, [None], quoting=csv.QUOTE_NONE)
    Test_Csv._write_error_test(OSError, test_csv.BadIterable())

    class BadList:

        def __len__(Test_Csv):
            return 10

        def __getitem__(Test_Csv, i):
            if i > 2:
                raise OSError
    Test_Csv._write_error_test(OSError, BadList())

    class BadItem:

        def __str__(Test_Csv):
            raise OSError
    Test_Csv._write_error_test(OSError, [BadItem()])

Test_Csv = test_csv.Test_Csv()
test_write_arg_valid()

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

def test_writer_arg_valid():
    Test_Csv._test_arg_valid(csv.writer, StringIO())

    class BadWriter:

        @property
        def write(Test_Csv):
            raise OSError
    Test_Csv.assertRaises(OSError, csv.writer, BadWriter())

Test_Csv = test_csv.Test_Csv()
test_writer_arg_valid()

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

def test_read_eol():
    Test_Csv._read_test(['a,b'], [['a', 'b']])
    Test_Csv._read_test(['a,b\n'], [['a', 'b']])
    Test_Csv._read_test(['a,b\r\n'], [['a', 'b']])
    Test_Csv._read_test(['a,b\r'], [['a', 'b']])
    Test_Csv.assertRaises(csv.Error, Test_Csv._read_test, ['a,b\rc,d'], [])
    Test_Csv.assertRaises(csv.Error, Test_Csv._read_test, ['a,b\nc,d'], [])
    Test_Csv.assertRaises(csv.Error, Test_Csv._read_test, ['a,b\r\nc,d'], [])

Test_Csv = test_csv.Test_Csv()
test_read_eol()

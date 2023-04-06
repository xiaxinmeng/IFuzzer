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

def test_read_quoting():
    Test_Csv._read_test(['1,",3,",5'], [['1', ',3,', '5']])
    Test_Csv._read_test(['1,",3,",5'], [['1', '"', '3', '"', '5']], quotechar=None, escapechar='\\')
    Test_Csv._read_test(['1,",3,",5'], [['1', '"', '3', '"', '5']], quoting=csv.QUOTE_NONE, escapechar='\\')
    Test_Csv._read_test([',3,"5",7.3, 9'], [['', 3, '5', 7.3, 9]], quoting=csv.QUOTE_NONNUMERIC)
    Test_Csv._read_test(['"a\nb", 7'], [['a\nb', ' 7']])
    Test_Csv.assertRaises(ValueError, Test_Csv._read_test, ['abc,3'], [[]], quoting=csv.QUOTE_NONNUMERIC)

Test_Csv = test_csv.Test_Csv()
test_read_quoting()

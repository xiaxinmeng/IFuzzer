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

def test_read_oddinputs():
    Test_Csv._read_test([], [])
    Test_Csv._read_test([''], [[]])
    Test_Csv.assertRaises(csv.Error, Test_Csv._read_test, ['"ab"c'], None, strict=1)
    Test_Csv.assertRaises(csv.Error, Test_Csv._read_test, ['ab\x00c'], None, strict=1)
    Test_Csv._read_test(['"ab"c'], [['abc']], doublequote=0)
    Test_Csv.assertRaises(csv.Error, Test_Csv._read_test, [b'ab\x00c'], None)

Test_Csv = test_csv.Test_Csv()
test_read_oddinputs()

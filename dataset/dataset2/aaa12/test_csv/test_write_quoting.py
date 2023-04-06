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

def test_write_quoting():
    Test_Csv._write_test(['a', 1, 'p,q'], 'a,1,"p,q"')
    Test_Csv._write_error_test(csv.Error, ['a', 1, 'p,q'], quoting=csv.QUOTE_NONE)
    Test_Csv._write_test(['a', 1, 'p,q'], 'a,1,"p,q"', quoting=csv.QUOTE_MINIMAL)
    Test_Csv._write_test(['a', 1, 'p,q'], '"a",1,"p,q"', quoting=csv.QUOTE_NONNUMERIC)
    Test_Csv._write_test(['a', 1, 'p,q'], '"a","1","p,q"', quoting=csv.QUOTE_ALL)
    Test_Csv._write_test(['a\nb', 1], '"a\nb","1"', quoting=csv.QUOTE_ALL)

Test_Csv = test_csv.Test_Csv()
test_write_quoting()

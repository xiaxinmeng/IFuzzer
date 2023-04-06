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

def test_write_escape():
    Test_Csv._write_test(['a', 1, 'p,q'], 'a,1,"p,q"', escapechar='\\')
    Test_Csv._write_error_test(csv.Error, ['a', 1, 'p,"q"'], escapechar=None, doublequote=False)
    Test_Csv._write_test(['a', 1, 'p,"q"'], 'a,1,"p,\\"q\\""', escapechar='\\', doublequote=False)
    Test_Csv._write_test(['"'], '""""', escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    Test_Csv._write_test(['"'], '\\"', escapechar='\\', quoting=csv.QUOTE_MINIMAL, doublequote=False)
    Test_Csv._write_test(['"'], '\\"', escapechar='\\', quoting=csv.QUOTE_NONE)
    Test_Csv._write_test(['a', 1, 'p,q'], 'a,1,p\\,q', escapechar='\\', quoting=csv.QUOTE_NONE)
    Test_Csv._write_test(['\\', 'a'], '\\\\,a', escapechar='\\', quoting=csv.QUOTE_NONE)
    Test_Csv._write_test(['\\', 'a'], '\\\\,a', escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    Test_Csv._write_test(['\\', 'a'], '"\\\\","a"', escapechar='\\', quoting=csv.QUOTE_ALL)
    Test_Csv._write_test(['\\ ', 'a'], '\\\\ ,a', escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    Test_Csv._write_test(['\\,', 'a'], '\\\\\\,,a', escapechar='\\', quoting=csv.QUOTE_NONE)
    Test_Csv._write_test([',\\', 'a'], '",\\\\",a', escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    Test_Csv._write_test(['C\\', '6', '7', 'X"'], 'C\\\\,6,7,"X"""', escapechar='\\', quoting=csv.QUOTE_MINIMAL)

Test_Csv = test_csv.Test_Csv()
test_write_escape()

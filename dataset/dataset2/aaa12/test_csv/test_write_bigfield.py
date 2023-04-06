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

def test_write_bigfield():
    bigstring = 'X' * 50000
    Test_Csv._write_test([bigstring, bigstring], '%s,%s' % (bigstring, bigstring))

Test_Csv = test_csv.Test_Csv()
test_write_bigfield()

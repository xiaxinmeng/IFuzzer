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

def test_quoted_nl():
    input = '1,2,3,"""I see,""\nsaid the blind man","as he picked up his\nhammer and saw"\n9,8,7,6'
    TestDialectExcel.readerAssertEqual(input, [['1', '2', '3', '"I see,"\nsaid the blind man', 'as he picked up his\nhammer and saw'], ['9', '8', '7', '6']])

TestDialectExcel = test_csv.TestDialectExcel()
test_quoted_nl()

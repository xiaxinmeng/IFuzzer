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

def test_sniff():
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(TestSniffer.sample1)
    TestSniffer.assertEqual(dialect.delimiter, ',')
    TestSniffer.assertEqual(dialect.quotechar, '"')
    TestSniffer.assertIs(dialect.skipinitialspace, True)
    dialect = sniffer.sniff(TestSniffer.sample2)
    TestSniffer.assertEqual(dialect.delimiter, ':')
    TestSniffer.assertEqual(dialect.quotechar, "'")
    TestSniffer.assertIs(dialect.skipinitialspace, False)

TestSniffer = test_csv.TestSniffer()
test_sniff()

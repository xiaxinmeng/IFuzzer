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

def test_guess_quote_and_delimiter():
    sniffer = csv.Sniffer()
    for header in (";'123;4';", "'123;4';", ";'123;4'", "'123;4'"):
        with TestSniffer.subTest(header):
            dialect = sniffer.sniff(header, ',;')
            TestSniffer.assertEqual(dialect.delimiter, ';')
            TestSniffer.assertEqual(dialect.quotechar, "'")
            TestSniffer.assertIs(dialect.doublequote, False)
            TestSniffer.assertIs(dialect.skipinitialspace, False)

TestSniffer = test_csv.TestSniffer()
test_guess_quote_and_delimiter()

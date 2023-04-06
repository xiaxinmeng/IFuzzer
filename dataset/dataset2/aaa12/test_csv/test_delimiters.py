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

def test_delimiters():
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(TestSniffer.sample3)
    TestSniffer.assertIn(dialect.delimiter, TestSniffer.sample3)
    dialect = sniffer.sniff(TestSniffer.sample3, delimiters='?,')
    TestSniffer.assertEqual(dialect.delimiter, '?')
    dialect = sniffer.sniff(TestSniffer.sample3, delimiters='/,')
    TestSniffer.assertEqual(dialect.delimiter, '/')
    dialect = sniffer.sniff(TestSniffer.sample4)
    TestSniffer.assertEqual(dialect.delimiter, ';')
    dialect = sniffer.sniff(TestSniffer.sample5)
    TestSniffer.assertEqual(dialect.delimiter, '\t')
    dialect = sniffer.sniff(TestSniffer.sample6)
    TestSniffer.assertEqual(dialect.delimiter, '|')
    dialect = sniffer.sniff(TestSniffer.sample7)
    TestSniffer.assertEqual(dialect.delimiter, '|')
    TestSniffer.assertEqual(dialect.quotechar, "'")
    dialect = sniffer.sniff(TestSniffer.sample8)
    TestSniffer.assertEqual(dialect.delimiter, '+')
    dialect = sniffer.sniff(TestSniffer.sample9)
    TestSniffer.assertEqual(dialect.delimiter, '+')
    TestSniffer.assertEqual(dialect.quotechar, "'")

TestSniffer = test_csv.TestSniffer()
test_delimiters()

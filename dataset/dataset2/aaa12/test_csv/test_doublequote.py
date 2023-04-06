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

def test_doublequote():
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(TestSniffer.header1)
    TestSniffer.assertFalse(dialect.doublequote)
    dialect = sniffer.sniff(TestSniffer.header2)
    TestSniffer.assertFalse(dialect.doublequote)
    dialect = sniffer.sniff(TestSniffer.sample2)
    TestSniffer.assertTrue(dialect.doublequote)
    dialect = sniffer.sniff(TestSniffer.sample8)
    TestSniffer.assertFalse(dialect.doublequote)
    dialect = sniffer.sniff(TestSniffer.sample9)
    TestSniffer.assertTrue(dialect.doublequote)

TestSniffer = test_csv.TestSniffer()
test_doublequote()

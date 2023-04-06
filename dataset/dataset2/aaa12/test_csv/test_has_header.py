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

def test_has_header():
    sniffer = csv.Sniffer()
    TestSniffer.assertIs(sniffer.has_header(TestSniffer.sample1), False)
    TestSniffer.assertIs(sniffer.has_header(TestSniffer.header1 + TestSniffer.sample1), True)

TestSniffer = test_csv.TestSniffer()
test_has_header()

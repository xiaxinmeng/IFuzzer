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

def test_dialect_apply():

    class testA(csv.excel):
        delimiter = '\t'

    class testB(csv.excel):
        delimiter = ':'

    class testC(csv.excel):
        delimiter = '|'

    class testUni(csv.excel):
        delimiter = 'Λ'
    csv.register_dialect('testC', testC)
    try:
        TestDialectRegistry.compare_dialect_123('1,2,3\r\n')
        TestDialectRegistry.compare_dialect_123('1\t2\t3\r\n', testA)
        TestDialectRegistry.compare_dialect_123('1:2:3\r\n', dialect=testB())
        TestDialectRegistry.compare_dialect_123('1|2|3\r\n', dialect='testC')
        TestDialectRegistry.compare_dialect_123('1;2;3\r\n', dialect=testA, delimiter=';')
        TestDialectRegistry.compare_dialect_123('1Λ2Λ3\r\n', dialect=testUni)
    finally:
        csv.unregister_dialect('testC')

TestDialectRegistry = test_csv.TestDialectRegistry()
test_dialect_apply()

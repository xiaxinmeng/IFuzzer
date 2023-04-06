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

def test_typo_in_extrasaction_raises_error():
    fileobj = StringIO()
    TestDictFields.assertRaises(ValueError, csv.DictWriter, fileobj, ['f1', 'f2'], extrasaction='raised')

TestDictFields = test_csv.TestDictFields()
test_typo_in_extrasaction_raises_error()

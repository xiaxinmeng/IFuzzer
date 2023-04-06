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

def test_ordered_dict_reader():
    data = dedent('            FirstName,LastName\n            Eric,Idle\n            Graham,Chapman,Over1,Over2\n\n            Under1\n            John,Cleese\n        ').splitlines()
    KeyOrderingTest.assertEqual(list(csv.DictReader(data)), [OrderedDict([('FirstName', 'Eric'), ('LastName', 'Idle')]), OrderedDict([('FirstName', 'Graham'), ('LastName', 'Chapman'), (None, ['Over1', 'Over2'])]), OrderedDict([('FirstName', 'Under1'), ('LastName', None)]), OrderedDict([('FirstName', 'John'), ('LastName', 'Cleese')])])
    KeyOrderingTest.assertEqual(list(csv.DictReader(data, restkey='OtherInfo')), [OrderedDict([('FirstName', 'Eric'), ('LastName', 'Idle')]), OrderedDict([('FirstName', 'Graham'), ('LastName', 'Chapman'), ('OtherInfo', ['Over1', 'Over2'])]), OrderedDict([('FirstName', 'Under1'), ('LastName', None)]), OrderedDict([('FirstName', 'John'), ('LastName', 'Cleese')])])
    del data[0]
    KeyOrderingTest.assertEqual(list(csv.DictReader(data, fieldnames=['fname', 'lname'])), [OrderedDict([('fname', 'Eric'), ('lname', 'Idle')]), OrderedDict([('fname', 'Graham'), ('lname', 'Chapman'), (None, ['Over1', 'Over2'])]), OrderedDict([('fname', 'Under1'), ('lname', None)]), OrderedDict([('fname', 'John'), ('lname', 'Cleese')])])

KeyOrderingTest = test_csv.KeyOrderingTest()
test_ordered_dict_reader()

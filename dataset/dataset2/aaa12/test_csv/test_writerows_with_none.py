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

def test_writerows_with_none():
    with TemporaryFile('w+', newline='') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerows([['a', None], [None, 'd']])
        fileobj.seek(0)
        Test_Csv.assertEqual(fileobj.read(), 'a,\r\n,d\r\n')
    with TemporaryFile('w+', newline='') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerows([[None], ['a']])
        fileobj.seek(0)
        Test_Csv.assertEqual(fileobj.read(), '""\r\na\r\n')
    with TemporaryFile('w+', newline='') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerows([['a'], [None]])
        fileobj.seek(0)
        Test_Csv.assertEqual(fileobj.read(), 'a\r\n""\r\n')

Test_Csv = test_csv.Test_Csv()
test_writerows_with_none()

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

def test_writerows():

    class BrokenFile:

        def write(Test_Csv, buf):
            raise OSError
    writer = csv.writer(test_csv.BrokenFile())
    Test_Csv.assertRaises(OSError, writer.writerows, [['a']])
    with TemporaryFile('w+', newline='') as fileobj:
        writer = csv.writer(fileobj)
        Test_Csv.assertRaises(TypeError, writer.writerows, None)
        writer.writerows([['a', 'b'], ['c', 'd']])
        fileobj.seek(0)
        Test_Csv.assertEqual(fileobj.read(), 'a,b\r\nc,d\r\n')

Test_Csv = test_csv.Test_Csv()
test_writerows()

import collections
import configparser
import io
import os
import pathlib
import textwrap
import unittest
import warnings
from test import support
from test.support import os_helper
import decimal
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import pickle
import decimal
import test_configparser

def test_sorted():
    cf = SortedTestCase.fromstring('[b]\no4=1\no3=2\no2=3\no1=4\n[a]\nk=v\n')
    output = io.StringIO()
    cf.write(output)
    SortedTestCase.assertEqual(output.getvalue(), '[a]\nk = v\n\n[b]\no1 = 4\no2 = 3\no3 = 2\no4 = 1\n\n')

SortedTestCase = test_configparser.SortedTestCase()
test_sorted()

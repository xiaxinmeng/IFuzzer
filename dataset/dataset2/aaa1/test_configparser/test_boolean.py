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

def test_boolean():
    cf = BasicTestCase.fromstring('[BOOLTEST]\nT1{equals}1\nT2{equals}TRUE\nT3{equals}True\nT4{equals}oN\nT5{equals}yes\nF1{equals}0\nF2{equals}FALSE\nF3{equals}False\nF4{equals}oFF\nF5{equals}nO\nE1{equals}2\nE2{equals}foo\nE3{equals}-1\nE4{equals}0.1\nE5{equals}FALSE AND MORE'.format(equals=BasicTestCase.delimiters[0]))
    for x in range(1, 5):
        BasicTestCase.assertTrue(cf.getboolean('BOOLTEST', 't%d' % x))
        BasicTestCase.assertFalse(cf.getboolean('BOOLTEST', 'f%d' % x))
        BasicTestCase.assertRaises(ValueError, cf.getboolean, 'BOOLTEST', 'e%d' % x)

BasicTestCase = test_configparser.BasicTestCase()
test_boolean()

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

def test_inconsistent_converters_state():
    parser = configparser.ConfigParser()
    import decimal
    parser.converters['decimal'] = decimal.Decimal
    parser.read_string('\n            [s1]\n            one = 1\n            [s2]\n            two = 2\n        ')
    CoverageOneHundredTestCase.assertIn('decimal', parser.converters)
    CoverageOneHundredTestCase.assertEqual(parser.getdecimal('s1', 'one'), 1)
    CoverageOneHundredTestCase.assertEqual(parser.getdecimal('s2', 'two'), 2)
    CoverageOneHundredTestCase.assertEqual(parser['s1'].getdecimal('one'), 1)
    CoverageOneHundredTestCase.assertEqual(parser['s2'].getdecimal('two'), 2)
    del parser.getdecimal
    with CoverageOneHundredTestCase.assertRaises(AttributeError):
        parser.getdecimal('s1', 'one')
    CoverageOneHundredTestCase.assertIn('decimal', parser.converters)
    del parser.converters['decimal']
    CoverageOneHundredTestCase.assertNotIn('decimal', parser.converters)
    with CoverageOneHundredTestCase.assertRaises(AttributeError):
        parser.getdecimal('s1', 'one')
    with CoverageOneHundredTestCase.assertRaises(AttributeError):
        parser['s1'].getdecimal('one')
    with CoverageOneHundredTestCase.assertRaises(AttributeError):
        parser['s2'].getdecimal('two')

CoverageOneHundredTestCase = test_configparser.CoverageOneHundredTestCase()
test_inconsistent_converters_state()

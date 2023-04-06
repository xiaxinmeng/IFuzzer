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

def test_invalid_multiline_value():
    if BasicTestCase.allow_no_value:
        BasicTestCase.skipTest('if no_value is allowed, ParsingError is not raised')
    invalid = textwrap.dedent('            [DEFAULT]\n            test {0} test\n            invalid'.format(BasicTestCase.delimiters[0]))
    cf = BasicTestCase.newconfig()
    with BasicTestCase.assertRaises(configparser.ParsingError):
        cf.read_string(invalid)
    BasicTestCase.assertEqual(cf.get('DEFAULT', 'test'), 'test')
    BasicTestCase.assertEqual(cf['DEFAULT']['test'], 'test')

BasicTestCase = test_configparser.BasicTestCase()
test_invalid_multiline_value()

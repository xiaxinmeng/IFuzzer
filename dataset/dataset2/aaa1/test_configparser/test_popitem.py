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

def test_popitem():
    cf = BasicTestCase.fromstring('\n            [section1]\n            name1 {0[0]} value1\n            [section2]\n            name2 {0[0]} value2\n            [section3]\n            name3 {0[0]} value3\n        '.format(BasicTestCase.delimiters), defaults={'default': '<default>'})
    BasicTestCase.assertEqual(cf.popitem()[0], 'section1')
    BasicTestCase.assertEqual(cf.popitem()[0], 'section2')
    BasicTestCase.assertEqual(cf.popitem()[0], 'section3')
    with BasicTestCase.assertRaises(KeyError):
        cf.popitem()

BasicTestCase = test_configparser.BasicTestCase()
test_popitem()

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

def test_interpolation_validation():
    parser = configparser.ConfigParser()
    parser.read_string('\n            [section]\n            invalid_percent = %\n            invalid_reference = %(()\n            invalid_variable = %(does_not_exist)s\n        ')
    with CoverageOneHundredTestCase.assertRaises(configparser.InterpolationSyntaxError) as cm:
        parser['section']['invalid_percent']
    CoverageOneHundredTestCase.assertEqual(str(cm.exception), "'%' must be followed by '%' or '(', found: '%'")
    with CoverageOneHundredTestCase.assertRaises(configparser.InterpolationSyntaxError) as cm:
        parser['section']['invalid_reference']
    CoverageOneHundredTestCase.assertEqual(str(cm.exception), "bad interpolation variable reference '%(()'")

CoverageOneHundredTestCase = test_configparser.CoverageOneHundredTestCase()
test_interpolation_validation()

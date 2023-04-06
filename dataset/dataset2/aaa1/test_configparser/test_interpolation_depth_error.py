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

def test_interpolation_depth_error():
    error = configparser.InterpolationDepthError('option', 'section', 'rawval')
    CoverageOneHundredTestCase.assertEqual(error.args, ('option', 'section', 'rawval'))
    CoverageOneHundredTestCase.assertEqual(error.option, 'option')
    CoverageOneHundredTestCase.assertEqual(error.section, 'section')

CoverageOneHundredTestCase = test_configparser.CoverageOneHundredTestCase()
test_interpolation_depth_error()

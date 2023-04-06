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

def test_duplicate_option_error():
    error = configparser.DuplicateOptionError('section', 'option')
    CoverageOneHundredTestCase.assertEqual(error.section, 'section')
    CoverageOneHundredTestCase.assertEqual(error.option, 'option')
    CoverageOneHundredTestCase.assertEqual(error.source, None)
    CoverageOneHundredTestCase.assertEqual(error.lineno, None)
    CoverageOneHundredTestCase.assertEqual(error.args, ('section', 'option', None, None))
    CoverageOneHundredTestCase.assertEqual(str(error), "Option 'option' in section 'section' already exists")

CoverageOneHundredTestCase = test_configparser.CoverageOneHundredTestCase()
test_duplicate_option_error()

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

def test_safeconfigparser_deprecation():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always', DeprecationWarning)
        parser = configparser.SafeConfigParser()
    for warning in w:
        CoverageOneHundredTestCase.assertTrue(warning.category is DeprecationWarning)

CoverageOneHundredTestCase = test_configparser.CoverageOneHundredTestCase()
test_safeconfigparser_deprecation()

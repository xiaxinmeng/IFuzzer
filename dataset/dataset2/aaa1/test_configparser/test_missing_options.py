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

def test_missing_options():
    parser = configparser.ConfigParser()
    parser.read_string('\n        [Paths]\n        home_dir: /Users\n        ')
    with ExceptionContextTestCase.assertRaises(configparser.NoSectionError) as cm:
        parser.options('test')
    ExceptionContextTestCase.assertIs(cm.exception.__suppress_context__, True)

ExceptionContextTestCase = test_configparser.ExceptionContextTestCase()
test_missing_options()

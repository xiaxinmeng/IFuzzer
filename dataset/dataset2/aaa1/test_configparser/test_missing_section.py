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

def test_missing_section():
    config = configparser.ConfigParser()
    with ExceptionContextTestCase.assertRaises(configparser.NoSectionError) as cm:
        config.set('Section1', 'an_int', '15')
    ExceptionContextTestCase.assertIs(cm.exception.__suppress_context__, True)

ExceptionContextTestCase = test_configparser.ExceptionContextTestCase()
test_missing_section()

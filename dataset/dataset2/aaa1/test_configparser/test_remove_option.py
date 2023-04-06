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

def test_remove_option():
    config = configparser.ConfigParser()
    with ExceptionContextTestCase.assertRaises(configparser.NoSectionError) as cm:
        config.remove_option('Section1', 'an_int')
    ExceptionContextTestCase.assertIs(cm.exception.__suppress_context__, True)

ExceptionContextTestCase = test_configparser.ExceptionContextTestCase()
test_remove_option()

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

def test_get_extended_interpolation():
    parser = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    parser.read_string('\n        [Paths]\n        home_dir: /Users\n        my_dir: ${home_dir1}/lumberjack\n        my_pictures: ${my_dir}/Pictures\n        ')
    cm = ExceptionContextTestCase.assertRaises(configparser.InterpolationMissingOptionError)
    with cm:
        parser.get('Paths', 'my_dir')
    ExceptionContextTestCase.assertIs(cm.exception.__suppress_context__, True)

ExceptionContextTestCase = test_configparser.ExceptionContextTestCase()
test_get_extended_interpolation()

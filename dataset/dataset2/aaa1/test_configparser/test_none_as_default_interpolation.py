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

def test_none_as_default_interpolation():

    class CustomConfigParser(configparser.ConfigParser):
        _DEFAULT_INTERPOLATION = None
    cf = CustomConfigParser()
    cf.read_string(ConfigParserTestCaseNoInterpolation.ini)
    ConfigParserTestCaseNoInterpolation.assertMatchesIni(cf)

ConfigParserTestCaseNoInterpolation = test_configparser.ConfigParserTestCaseNoInterpolation()
test_none_as_default_interpolation()

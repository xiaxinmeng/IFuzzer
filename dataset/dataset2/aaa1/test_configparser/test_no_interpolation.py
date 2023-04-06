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

def test_no_interpolation():
    cf = ConfigParserTestCaseNoInterpolation.fromstring(ConfigParserTestCaseNoInterpolation.ini)
    ConfigParserTestCaseNoInterpolation.assertMatchesIni(cf)

ConfigParserTestCaseNoInterpolation = test_configparser.ConfigParserTestCaseNoInterpolation()
test_no_interpolation()

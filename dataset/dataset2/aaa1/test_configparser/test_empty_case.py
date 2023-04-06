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

def test_empty_case():
    cf = ConfigParserTestCaseNoInterpolation.newconfig()
    ConfigParserTestCaseNoInterpolation.assertIsNone(cf.read_string(''))

ConfigParserTestCaseNoInterpolation = test_configparser.ConfigParserTestCaseNoInterpolation()
test_empty_case()

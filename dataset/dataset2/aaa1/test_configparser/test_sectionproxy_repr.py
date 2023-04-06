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

def test_sectionproxy_repr():
    parser = configparser.ConfigParser()
    parser.read_string('\n            [section]\n            key = value\n        ')
    CoverageOneHundredTestCase.assertEqual(repr(parser['section']), '<Section: section>')

CoverageOneHundredTestCase = test_configparser.CoverageOneHundredTestCase()
test_sectionproxy_repr()

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

def test_add_section_default():
    cf = ConfigParserTestCase.newconfig()
    ConfigParserTestCase.assertRaises(ValueError, cf.add_section, ConfigParserTestCase.default_section)

ConfigParserTestCase = test_configparser.ConfigParserTestCase()
test_add_section_default()

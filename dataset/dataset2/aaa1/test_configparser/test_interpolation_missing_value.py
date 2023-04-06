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

def test_interpolation_missing_value():
    cf = ConfigParserTestCase.get_interpolation_config()
    e = ConfigParserTestCase.get_error(cf, configparser.InterpolationMissingOptionError, 'Interpolation Error', 'name')
    ConfigParserTestCase.assertEqual(e.reference, 'reference')
    ConfigParserTestCase.assertEqual(e.section, 'Interpolation Error')
    ConfigParserTestCase.assertEqual(e.option, 'name')
    if ConfigParserTestCase.interpolation == configparser._UNSET:
        ConfigParserTestCase.assertEqual(e.args, ('name', 'Interpolation Error', '%(reference)s', 'reference'))
    elif isinstance(ConfigParserTestCase.interpolation, configparser.LegacyInterpolation):
        ConfigParserTestCase.assertEqual(e.args, ('name', 'Interpolation Error', '%(reference)s', 'reference'))

ConfigParserTestCase = test_configparser.ConfigParserTestCase()
test_interpolation_missing_value()

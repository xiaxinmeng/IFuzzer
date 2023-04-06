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

def test_defaults_keyword():
    """bpo-23835 legacy behavior for RawConfigParser"""
    with ConfigParserTestCase.assertRaises(AttributeError) as ctx:
        ConfigParserTestCase.newconfig(defaults={1: 2.4})
    err = ctx.exception
    ConfigParserTestCase.assertEqual(str(err), "'int' object has no attribute 'lower'")
    cf = ConfigParserTestCase.newconfig(defaults={'A': 5.2})
    ConfigParserTestCase.assertAlmostEqual(cf[ConfigParserTestCase.default_section]['a'], 5.2)

ConfigParserTestCase = test_configparser.ConfigParserTestCase()
test_defaults_keyword()

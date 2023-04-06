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

def test_safe_interpolation():
    cf = ConfigParserTestCase.fromstring('[section]\noption1{eq}xxx\noption2{eq}%(option1)s/xxx\nok{eq}%(option1)s/%%s\nnot_ok{eq}%(option2)s/%%s'.format(eq=ConfigParserTestCase.delimiters[0]))
    ConfigParserTestCase.assertEqual(cf.get('section', 'ok'), 'xxx/%s')
    if ConfigParserTestCase.interpolation == configparser._UNSET:
        ConfigParserTestCase.assertEqual(cf.get('section', 'not_ok'), 'xxx/xxx/%s')
    elif isinstance(ConfigParserTestCase.interpolation, configparser.LegacyInterpolation):
        with ConfigParserTestCase.assertRaises(TypeError):
            cf.get('section', 'not_ok')

ConfigParserTestCase = test_configparser.ConfigParserTestCase()
test_safe_interpolation()

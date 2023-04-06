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

def test_set_nonstring_types():
    cf = ConfigParserTestCase.newconfig()
    cf.add_section('non-string')
    cf.set('non-string', 'int', 1)
    cf.set('non-string', 'list', [0, 1, 1, 2, 3, 5, 8, 13])
    cf.set('non-string', 'dict', {'pi': 3.14159})
    ConfigParserTestCase.assertEqual(cf.get('non-string', 'int'), 1)
    ConfigParserTestCase.assertEqual(cf.get('non-string', 'list'), [0, 1, 1, 2, 3, 5, 8, 13])
    ConfigParserTestCase.assertEqual(cf.get('non-string', 'dict'), {'pi': 3.14159})
    cf.add_section(123)
    cf.set(123, 'this is sick', True)
    ConfigParserTestCase.assertEqual(cf.get(123, 'this is sick'), True)
    if cf._dict is configparser._default_dict:
        cf.optionxform = lambda x: x
        cf.set('non-string', 1, 1)
        ConfigParserTestCase.assertEqual(cf.get('non-string', 1), 1)

ConfigParserTestCase = test_configparser.ConfigParserTestCase()
test_set_nonstring_types()

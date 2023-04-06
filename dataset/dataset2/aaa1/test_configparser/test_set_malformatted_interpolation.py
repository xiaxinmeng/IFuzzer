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

def test_set_malformatted_interpolation():
    cf = ConfigParserTestCase.fromstring('[sect]\noption1{eq}foo\n'.format(eq=ConfigParserTestCase.delimiters[0]))
    ConfigParserTestCase.assertEqual(cf.get('sect', 'option1'), 'foo')
    cf.set('sect', 'option1', '%foo')
    ConfigParserTestCase.assertEqual(cf.get('sect', 'option1'), '%foo')
    cf.set('sect', 'option1', 'foo%')
    ConfigParserTestCase.assertEqual(cf.get('sect', 'option1'), 'foo%')
    cf.set('sect', 'option1', 'f%oo')
    ConfigParserTestCase.assertEqual(cf.get('sect', 'option1'), 'f%oo')
    cf.set('sect', 'option2', 'foo%%bar')
    ConfigParserTestCase.assertEqual(cf.get('sect', 'option2'), 'foo%%bar')

ConfigParserTestCase = test_configparser.ConfigParserTestCase()
test_set_malformatted_interpolation()

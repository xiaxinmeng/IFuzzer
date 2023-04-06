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

def test_cfgparser_dot_3():
    tricky = support.findfile('cfgparser.3')
    cf = ConfigParserTestCaseTrickyFile.newconfig()
    ConfigParserTestCaseTrickyFile.assertEqual(len(cf.read(tricky, encoding='utf-8')), 1)
    ConfigParserTestCaseTrickyFile.assertEqual(cf.sections(), ['strange', 'corruption', 'yeah, sections can be indented as well', 'another one!', 'no values here', 'tricky interpolation', 'more interpolation'])
    ConfigParserTestCaseTrickyFile.assertEqual(cf.getint(ConfigParserTestCaseTrickyFile.default_section, 'go', vars={'interpolate': '-1'}), -1)
    with ConfigParserTestCaseTrickyFile.assertRaises(ValueError):
        cf.getint(ConfigParserTestCaseTrickyFile.default_section, 'go', raw=True, vars={'interpolate': '-1'})
    ConfigParserTestCaseTrickyFile.assertEqual(len(cf.get('strange', 'other').split('\n')), 4)
    ConfigParserTestCaseTrickyFile.assertEqual(len(cf.get('corruption', 'value').split('\n')), 10)
    longname = 'yeah, sections can be indented as well'
    ConfigParserTestCaseTrickyFile.assertFalse(cf.getboolean(longname, 'are they subsections'))
    ConfigParserTestCaseTrickyFile.assertEqual(cf.get(longname, 'lets use some Unicode'), '片仮名')
    ConfigParserTestCaseTrickyFile.assertEqual(len(cf.items('another one!')), 5)
    with ConfigParserTestCaseTrickyFile.assertRaises(configparser.InterpolationMissingOptionError):
        cf.items('no values here')
    ConfigParserTestCaseTrickyFile.assertEqual(cf.get('tricky interpolation', 'lets'), 'do this')
    ConfigParserTestCaseTrickyFile.assertEqual(cf.get('tricky interpolation', 'lets'), cf.get('tricky interpolation', 'go'))
    ConfigParserTestCaseTrickyFile.assertEqual(cf.get('more interpolation', 'lets'), 'go shopping')

ConfigParserTestCaseTrickyFile = test_configparser.ConfigParserTestCaseTrickyFile()
test_cfgparser_dot_3()

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

def test_clear():
    cf = BasicTestCase.newconfig({'foo': 'Bar'})
    BasicTestCase.assertEqual(cf.get(BasicTestCase.default_section, 'Foo'), 'Bar', 'could not locate option, expecting case-insensitive option names')
    cf['zing'] = {'option1': 'value1', 'option2': 'value2'}
    BasicTestCase.assertEqual(cf.sections(), ['zing'])
    BasicTestCase.assertEqual(set(cf['zing'].keys()), {'option1', 'option2', 'foo'})
    cf.clear()
    BasicTestCase.assertEqual(set(cf.sections()), set())
    BasicTestCase.assertEqual(set(cf[BasicTestCase.default_section].keys()), {'foo'})

BasicTestCase = test_configparser.BasicTestCase()
test_clear()

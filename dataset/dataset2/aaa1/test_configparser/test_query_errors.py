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

def test_query_errors():
    cf = BasicTestCase.newconfig()
    BasicTestCase.assertEqual(cf.sections(), [], 'new ConfigParser should have no defined sections')
    BasicTestCase.assertFalse(cf.has_section('Foo'), 'new ConfigParser should have no acknowledged sections')
    with BasicTestCase.assertRaises(configparser.NoSectionError):
        cf.options('Foo')
    with BasicTestCase.assertRaises(configparser.NoSectionError):
        cf.set('foo', 'bar', 'value')
    e = BasicTestCase.get_error(cf, configparser.NoSectionError, 'foo', 'bar')
    BasicTestCase.assertEqual(e.args, ('foo',))
    cf.add_section('foo')
    e = BasicTestCase.get_error(cf, configparser.NoOptionError, 'foo', 'bar')
    BasicTestCase.assertEqual(e.args, ('bar', 'foo'))

BasicTestCase = test_configparser.BasicTestCase()
test_query_errors()

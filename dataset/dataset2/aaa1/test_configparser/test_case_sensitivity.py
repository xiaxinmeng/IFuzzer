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

def test_case_sensitivity():
    cf = BasicTestCase.newconfig()
    cf.add_section('A')
    cf.add_section('a')
    cf.add_section('B')
    L = cf.sections()
    L.sort()
    eq = BasicTestCase.assertEqual
    eq(L, ['A', 'B', 'a'])
    cf.set('a', 'B', 'value')
    eq(cf.options('a'), ['b'])
    eq(cf.get('a', 'b'), 'value', 'could not locate option, expecting case-insensitive option names')
    with BasicTestCase.assertRaises(configparser.NoSectionError):
        cf.set('b', 'A', 'value')
    BasicTestCase.assertTrue(cf.has_option('a', 'b'))
    BasicTestCase.assertFalse(cf.has_option('b', 'b'))
    cf.set('A', 'A-B', 'A-B value')
    for opt in ('a-b', 'A-b', 'a-B', 'A-B'):
        BasicTestCase.assertTrue(cf.has_option('A', opt), 'has_option() returned false for option which should exist')
    eq(cf.options('A'), ['a-b'])
    eq(cf.options('a'), ['b'])
    cf.remove_option('a', 'B')
    eq(cf.options('a'), [])
    cf = BasicTestCase.fromstring('[MySection]\nOption{} first line   \n\tsecond line   \n'.format(BasicTestCase.delimiters[0]))
    eq(cf.options('MySection'), ['option'])
    eq(cf.get('MySection', 'Option'), 'first line\nsecond line')
    cf = BasicTestCase.fromstring('[section]\nnekey{}nevalue\n'.format(BasicTestCase.delimiters[0]), defaults={'key': 'value'})
    BasicTestCase.assertTrue(cf.has_option('section', 'Key'))

BasicTestCase = test_configparser.BasicTestCase()
test_case_sensitivity()

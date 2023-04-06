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

def test_default_case_sensitivity():
    cf = BasicTestCase.newconfig({'foo': 'Bar'})
    BasicTestCase.assertEqual(cf.get(BasicTestCase.default_section, 'Foo'), 'Bar', 'could not locate option, expecting case-insensitive option names')
    cf = BasicTestCase.newconfig({'Foo': 'Bar'})
    BasicTestCase.assertEqual(cf.get(BasicTestCase.default_section, 'Foo'), 'Bar', 'could not locate option, expecting case-insensitive defaults')

BasicTestCase = test_configparser.BasicTestCase()
test_default_case_sensitivity()

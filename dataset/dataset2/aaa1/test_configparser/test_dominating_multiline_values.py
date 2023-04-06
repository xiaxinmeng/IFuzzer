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

def test_dominating_multiline_values():
    cf_from_file = MultilineValuesTestCase.newconfig()
    with open(os_helper.TESTFN) as f:
        cf_from_file.read_file(f)
    MultilineValuesTestCase.assertEqual(cf_from_file.get('section8', 'lovely_spam4'), MultilineValuesTestCase.wonderful_spam.replace('\t\n', '\n'))

MultilineValuesTestCase = test_configparser.MultilineValuesTestCase()
test_dominating_multiline_values()

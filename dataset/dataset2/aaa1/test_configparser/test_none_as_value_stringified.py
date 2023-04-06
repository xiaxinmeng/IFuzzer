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

def test_none_as_value_stringified():
    cp = configparser.ConfigParser(allow_no_value=False)
    cp.add_section('section')
    with Issue7005TestCase.assertRaises(TypeError):
        cp.set('section', 'option', None)

Issue7005TestCase = test_configparser.Issue7005TestCase()
test_none_as_value_stringified()

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

def test_none_as_value_stringified_raw():
    output = Issue7005TestCase.prepare(configparser.RawConfigParser)
    Issue7005TestCase.assertEqual(output, Issue7005TestCase.expected_output)

Issue7005TestCase = test_configparser.Issue7005TestCase()
test_none_as_value_stringified_raw()

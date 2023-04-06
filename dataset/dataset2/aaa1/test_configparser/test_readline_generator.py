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

def test_readline_generator():
    """Issue #11670."""
    parser = configparser.ConfigParser()
    with ReadFileTestCase.assertRaises(TypeError):
        parser.read_file(test_configparser.FakeFile())
    parser.read_file(test_configparser.readline_generator(test_configparser.FakeFile()))
    ReadFileTestCase.assertIn('Foo Bar', parser)
    ReadFileTestCase.assertIn('foo', parser['Foo Bar'])
    ReadFileTestCase.assertEqual(parser['Foo Bar']['foo'], 'newbar')

ReadFileTestCase = test_configparser.ReadFileTestCase()
test_readline_generator()

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

def test_iterable():
    lines = textwrap.dedent('\n        [Foo Bar]\n        foo=newbar').strip().split('\n')
    parser = configparser.ConfigParser()
    parser.read_file(lines)
    ReadFileTestCase.assertIn('Foo Bar', parser)
    ReadFileTestCase.assertIn('foo', parser['Foo Bar'])
    ReadFileTestCase.assertEqual(parser['Foo Bar']['foo'], 'newbar')

ReadFileTestCase = test_configparser.ReadFileTestCase()
test_iterable()

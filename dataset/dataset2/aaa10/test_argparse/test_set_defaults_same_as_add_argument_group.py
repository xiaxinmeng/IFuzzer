import inspect
import os
import shutil
import stat
import sys
import textwrap
import tempfile
import unittest
import argparse
from io import StringIO
from test import support
from test.support import os_helper
from unittest import mock
import test_argparse

def test_set_defaults_same_as_add_argument_group():
    parser = test_argparse.ErrorRaisingArgumentParser()
    parser.set_defaults(w='W', x='X', y='Y', z='Z')
    group = parser.add_argument_group('foo')
    group.add_argument('-w')
    group.add_argument('-x', default='XX')
    group.add_argument('y', nargs='?')
    group.add_argument('z', nargs='?', default='ZZ')
    TestSetDefaults.assertEqual(test_argparse.NS(w='W', x='XX', y='Y', z='ZZ'), parser.parse_args([]))
    parser.set_defaults(w='WW', x='X', y='YY', z='Z')
    TestSetDefaults.assertEqual(test_argparse.NS(w='WW', x='X', y='YY', z='Z'), parser.parse_args([]))

TestSetDefaults = test_argparse.TestSetDefaults()
test_set_defaults_same_as_add_argument_group()

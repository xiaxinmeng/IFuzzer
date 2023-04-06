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

def test_set_defaults_with_args():
    parser = test_argparse.ErrorRaisingArgumentParser()
    parser.set_defaults(x='foo', y='bar')
    parser.add_argument('-x', default='xfoox')
    TestSetDefaults.assertEqual(test_argparse.NS(x='xfoox', y='bar'), parser.parse_args([]))
    TestSetDefaults.assertEqual(test_argparse.NS(x='xfoox', y='bar'), parser.parse_args([], test_argparse.NS()))
    TestSetDefaults.assertEqual(test_argparse.NS(x='baz', y='bar'), parser.parse_args([], test_argparse.NS(x='baz')))
    TestSetDefaults.assertEqual(test_argparse.NS(x='1', y='bar'), parser.parse_args('-x 1'.split()))
    TestSetDefaults.assertEqual(test_argparse.NS(x='1', y='bar'), parser.parse_args('-x 1'.split(), test_argparse.NS()))
    TestSetDefaults.assertEqual(test_argparse.NS(x='1', y='bar'), parser.parse_args('-x 1'.split(), test_argparse.NS(x='baz')))

TestSetDefaults = test_argparse.TestSetDefaults()
test_set_defaults_with_args()

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

def test_set_defaults_no_args():
    parser = test_argparse.ErrorRaisingArgumentParser()
    parser.set_defaults(x='foo')
    parser.set_defaults(y='bar', z=1)
    TestSetDefaults.assertEqual(test_argparse.NS(x='foo', y='bar', z=1), parser.parse_args([]))
    TestSetDefaults.assertEqual(test_argparse.NS(x='foo', y='bar', z=1), parser.parse_args([], test_argparse.NS()))
    TestSetDefaults.assertEqual(test_argparse.NS(x='baz', y='bar', z=1), parser.parse_args([], test_argparse.NS(x='baz')))
    TestSetDefaults.assertEqual(test_argparse.NS(x='baz', y='bar', z=2), parser.parse_args([], test_argparse.NS(x='baz', z=2)))

TestSetDefaults = test_argparse.TestSetDefaults()
test_set_defaults_no_args()

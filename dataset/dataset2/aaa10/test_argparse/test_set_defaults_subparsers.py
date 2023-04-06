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

def test_set_defaults_subparsers():
    parser = test_argparse.ErrorRaisingArgumentParser()
    parser.set_defaults(x='foo')
    subparsers = parser.add_subparsers()
    parser_a = subparsers.add_parser('a')
    parser_a.set_defaults(y='bar')
    TestSetDefaults.assertEqual(test_argparse.NS(x='foo', y='bar'), parser.parse_args('a'.split()))

TestSetDefaults = test_argparse.TestSetDefaults()
test_set_defaults_subparsers()

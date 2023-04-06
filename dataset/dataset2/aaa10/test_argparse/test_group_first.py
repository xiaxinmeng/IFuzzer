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

def test_group_first():
    parser = test_argparse.ErrorRaisingArgumentParser()
    group = parser.add_argument_group('xxx')
    group.add_argument('foo')
    parser.add_argument('bar')
    parser.add_argument('baz')
    expected = test_argparse.NS(foo='1', bar='2', baz='3')
    result = parser.parse_args('1 2 3'.split())
    TestPositionalsGroups.assertEqual(expected, result)

TestPositionalsGroups = test_argparse.TestPositionalsGroups()
test_group_first()

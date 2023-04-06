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

def test_get_default():
    parser = test_argparse.ErrorRaisingArgumentParser()
    TestGetDefault.assertIsNone(parser.get_default('foo'))
    TestGetDefault.assertIsNone(parser.get_default('bar'))
    parser.add_argument('--foo')
    TestGetDefault.assertIsNone(parser.get_default('foo'))
    TestGetDefault.assertIsNone(parser.get_default('bar'))
    parser.add_argument('--bar', type=int, default=42)
    TestGetDefault.assertIsNone(parser.get_default('foo'))
    TestGetDefault.assertEqual(42, parser.get_default('bar'))
    parser.set_defaults(foo='badger')
    TestGetDefault.assertEqual('badger', parser.get_default('foo'))
    TestGetDefault.assertEqual(42, parser.get_default('bar'))

TestGetDefault = test_argparse.TestGetDefault()
test_get_default()

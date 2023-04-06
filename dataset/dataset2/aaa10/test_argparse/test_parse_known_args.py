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

def test_parse_known_args():
    TestAddSubparsers.assertEqual(TestAddSubparsers.parser.parse_known_args('0.5 1 b -w 7'.split()), (test_argparse.NS(foo=False, bar=0.5, w=7, x='b'), []))
    TestAddSubparsers.assertEqual(TestAddSubparsers.parser.parse_known_args('0.5 -p 1 b -w 7'.split()), (test_argparse.NS(foo=False, bar=0.5, w=7, x='b'), ['-p']))
    TestAddSubparsers.assertEqual(TestAddSubparsers.parser.parse_known_args('0.5 1 b -w 7 -p'.split()), (test_argparse.NS(foo=False, bar=0.5, w=7, x='b'), ['-p']))
    TestAddSubparsers.assertEqual(TestAddSubparsers.parser.parse_known_args('0.5 1 b -q -rs -w 7'.split()), (test_argparse.NS(foo=False, bar=0.5, w=7, x='b'), ['-q', '-rs']))
    TestAddSubparsers.assertEqual(TestAddSubparsers.parser.parse_known_args('0.5 -W 1 b -X Y -w 7 Z'.split()), (test_argparse.NS(foo=False, bar=0.5, w=7, x='b'), ['-W', '-X', 'Y', 'Z']))

TestAddSubparsers = test_argparse.TestAddSubparsers()
TestAddSubparsers.setUp()
test_parse_known_args()

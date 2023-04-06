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

def test_parse_args():
    TestAddSubparsers.assertEqual(TestAddSubparsers.parser.parse_args('0.5 1 b -w 7'.split()), test_argparse.NS(foo=False, bar=0.5, w=7, x='b'))
    TestAddSubparsers.assertEqual(TestAddSubparsers.parser.parse_args('0.25 --foo 2 -y 2 3j -- -1j'.split()), test_argparse.NS(foo=True, bar=0.25, y='2', z=[3j, -1j]))
    TestAddSubparsers.assertEqual(TestAddSubparsers.parser.parse_args('--foo 0.125 1 c'.split()), test_argparse.NS(foo=True, bar=0.125, w=None, x='c'))
    TestAddSubparsers.assertEqual(TestAddSubparsers.parser.parse_args('-1.5 3 11 -- a --foo 7 -- b'.split()), test_argparse.NS(foo=False, bar=-1.5, t=11, u=['a', '--foo', '7', '--', 'b']))

TestAddSubparsers = test_argparse.TestAddSubparsers()
TestAddSubparsers.setUp()
test_parse_args()

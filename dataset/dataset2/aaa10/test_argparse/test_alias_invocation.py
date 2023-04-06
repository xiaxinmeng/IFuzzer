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

def test_alias_invocation():
    parser = TestAddSubparsers._get_parser(aliases=True)
    TestAddSubparsers.assertEqual(parser.parse_known_args('0.5 1alias1 b'.split()), (test_argparse.NS(foo=False, bar=0.5, w=None, x='b'), []))
    TestAddSubparsers.assertEqual(parser.parse_known_args('0.5 1alias2 b'.split()), (test_argparse.NS(foo=False, bar=0.5, w=None, x='b'), []))

TestAddSubparsers = test_argparse.TestAddSubparsers()
test_alias_invocation()

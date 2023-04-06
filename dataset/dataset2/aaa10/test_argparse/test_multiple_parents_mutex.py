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

def test_multiple_parents_mutex():
    parents = [TestParentParsers.ab_mutex_parent, TestParentParsers.wxyz_parent]
    parser = test_argparse.ErrorRaisingArgumentParser(parents=parents)
    TestParentParsers.assertEqual(parser.parse_args('-a --w 2 3'.split()), test_argparse.NS(a=True, b=False, w='2', y=None, z='3'))
    TestParentParsers.assertArgumentParserError(parser.parse_args, '-a --w 2 3 -b'.split())
    TestParentParsers.assertArgumentParserError(parser.parse_args, '-a -b --w 2 3'.split())

TestParentParsers = test_argparse.TestParentParsers()
TestParentParsers.setUp()
test_multiple_parents_mutex()

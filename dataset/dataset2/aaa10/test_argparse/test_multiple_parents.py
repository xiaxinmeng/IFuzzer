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

def test_multiple_parents():
    parents = [TestParentParsers.abcd_parent, TestParentParsers.wxyz_parent]
    parser = test_argparse.ErrorRaisingArgumentParser(parents=parents)
    TestParentParsers.assertEqual(parser.parse_args('--d 1 --w 2 3 4'.split()), test_argparse.NS(a='3', b=None, d='1', w='2', y=None, z='4'))

TestParentParsers = test_argparse.TestParentParsers()
TestParentParsers.setUp()
test_multiple_parents()

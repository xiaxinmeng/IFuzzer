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

def test_same_argument_name_parents():
    parents = [TestParentParsers.wxyz_parent, TestParentParsers.z_parent]
    parser = test_argparse.ErrorRaisingArgumentParser(parents=parents)
    TestParentParsers.assertEqual(parser.parse_args('1 2'.split()), test_argparse.NS(w=None, y=None, z='2'))

TestParentParsers = test_argparse.TestParentParsers()
TestParentParsers.setUp()
test_same_argument_name_parents()

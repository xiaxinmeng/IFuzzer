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

def test_help():
    parser = test_argparse.ErrorRaisingArgumentParser(prog='PROG')
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('--foo', action='store_true')
    group1.add_argument('--bar', action='store_false')
    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument('--soup', action='store_true')
    group2.add_argument('--nuts', action='store_false')
    expected = '            usage: PROG [-h] [--foo | --bar] [--soup | --nuts]\n\n            options:\n              -h, --help  show this help message and exit\n              --foo\n              --bar\n              --soup\n              --nuts\n              '
    TestAddSubparsers.assertEqual(parser.format_help(), textwrap.dedent(expected))

TestAddSubparsers = test_argparse.TestAddSubparsers()
test_help()

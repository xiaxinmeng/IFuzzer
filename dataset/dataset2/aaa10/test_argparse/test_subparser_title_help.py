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

def test_subparser_title_help():
    parser = test_argparse.ErrorRaisingArgumentParser(prog='PROG', description='main description')
    parser.add_argument('--foo', action='store_true', help='foo help')
    parser.add_argument('bar', help='bar help')
    subparsers = parser.add_subparsers(title='subcommands', description='command help', help='additional text')
    parser1 = subparsers.add_parser('1')
    parser2 = subparsers.add_parser('2')
    TestAddSubparsers.assertEqual(parser.format_usage(), 'usage: PROG [-h] [--foo] bar {1,2} ...\n')
    TestAddSubparsers.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] [--foo] bar {1,2} ...\n\n            main description\n\n            positional arguments:\n              bar         bar help\n\n            options:\n              -h, --help  show this help message and exit\n              --foo       foo help\n\n            subcommands:\n              command help\n\n              {1,2}       additional text\n            '))

TestAddSubparsers = test_argparse.TestAddSubparsers()
test_subparser_title_help()

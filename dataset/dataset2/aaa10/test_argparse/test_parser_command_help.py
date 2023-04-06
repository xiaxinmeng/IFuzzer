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

def test_parser_command_help():
    TestAddSubparsers.assertEqual(TestAddSubparsers.command_help_parser.format_usage(), 'usage: PROG [-h] [--foo] bar {1,2,3} ...\n')
    TestAddSubparsers.assertEqual(TestAddSubparsers.command_help_parser.format_help(), textwrap.dedent('            usage: PROG [-h] [--foo] bar {1,2,3} ...\n\n            main description\n\n            positional arguments:\n              bar         bar help\n              {1,2,3}     command help\n                1         1 help\n                2         2 help\n                3         3 help\n\n            options:\n              -h, --help  show this help message and exit\n              --foo       foo help\n            '))

TestAddSubparsers = test_argparse.TestAddSubparsers()
TestAddSubparsers.setUp()
test_parser_command_help()

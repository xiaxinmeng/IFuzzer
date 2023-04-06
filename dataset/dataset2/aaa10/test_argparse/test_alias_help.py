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

def test_alias_help():
    parser = TestAddSubparsers._get_parser(aliases=True, subparser_help=True)
    TestAddSubparsers.maxDiff = None
    TestAddSubparsers.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] [--foo] bar COMMAND ...\n\n            main description\n\n            positional arguments:\n              bar                   bar help\n\n            options:\n              -h, --help            show this help message and exit\n              --foo                 foo help\n\n            commands:\n              COMMAND\n                1 (1alias1, 1alias2)\n                                    1 help\n                2                   2 help\n                3                   3 help\n            '))

TestAddSubparsers = test_argparse.TestAddSubparsers()
test_alias_help()

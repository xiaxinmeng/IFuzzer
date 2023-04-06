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

def test_help_non_breaking_spaces():
    parser = test_argparse.ErrorRaisingArgumentParser(prog='PROG', description='main description')
    parser.add_argument('--non-breaking', action='store_false', help='help message containing non-breaking spaces shall not wrap\xa0at non-breaking spaces')
    TestAddSubparsers.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] [--non-breaking]\n\n            main description\n\n            options:\n              -h, --help      show this help message and exit\n              --non-breaking  help message containing non-breaking spaces shall not\n                              wrap\xa0at non-breaking spaces\n        '))

TestAddSubparsers = test_argparse.TestAddSubparsers()
test_help_non_breaking_spaces()

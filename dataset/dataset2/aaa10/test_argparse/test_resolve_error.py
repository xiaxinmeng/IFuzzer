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

def test_resolve_error():
    get_parser = argparse.ArgumentParser
    parser = get_parser(prog='PROG', conflict_handler='resolve')
    parser.add_argument('-x', help='OLD X')
    parser.add_argument('-x', help='NEW X')
    TestConflictHandling.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] [-x X]\n\n            options:\n              -h, --help  show this help message and exit\n              -x X        NEW X\n            '))
    parser.add_argument('--spam', metavar='OLD_SPAM')
    parser.add_argument('--spam', metavar='NEW_SPAM')
    TestConflictHandling.assertEqual(parser.format_help(), textwrap.dedent('            usage: PROG [-h] [-x X] [--spam NEW_SPAM]\n\n            options:\n              -h, --help       show this help message and exit\n              -x X             NEW X\n              --spam NEW_SPAM\n            '))

TestConflictHandling = test_argparse.TestConflictHandling()
test_resolve_error()

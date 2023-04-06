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

def test_parent_help():
    parents = [TestParentParsers.abcd_parent, TestParentParsers.wxyz_parent]
    parser = test_argparse.ErrorRaisingArgumentParser(parents=parents)
    parser_help = parser.format_help()
    progname = TestParentParsers.main_program
    TestParentParsers.assertEqual(parser_help, textwrap.dedent('            usage: {}{}[-h] [-b B] [--d D] [--w W] [-y Y] a z\n\n            positional arguments:\n              a\n              z\n\n            options:\n              -h, --help  show this help message and exit\n              -b B\n              --w W\n\n            c:\n              --d D\n\n            x:\n              -y Y\n        '.format(progname, ' ' if progname else '')))

TestParentParsers = test_argparse.TestParentParsers()
TestParentParsers.setUp()
test_parent_help()

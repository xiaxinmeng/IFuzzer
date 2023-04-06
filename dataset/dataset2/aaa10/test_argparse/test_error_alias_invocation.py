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

def test_error_alias_invocation():
    parser = TestAddSubparsers._get_parser(aliases=True)
    TestAddSubparsers.assertArgumentParserError(parser.parse_args, '0.5 1alias3 b'.split())

TestAddSubparsers = test_argparse.TestAddSubparsers()
test_error_alias_invocation()

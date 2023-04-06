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

def test_parse_args_failures():
    for args_str in ['', 'a', 'a a', '0.5 a', '0.5 1', '0.5 1 -y', '0.5 2 -w']:
        args = args_str.split()
        TestAddSubparsers.assertArgumentParserError(TestAddSubparsers.parser.parse_args, args)

TestAddSubparsers = test_argparse.TestAddSubparsers()
TestAddSubparsers.setUp()
test_parse_args_failures()

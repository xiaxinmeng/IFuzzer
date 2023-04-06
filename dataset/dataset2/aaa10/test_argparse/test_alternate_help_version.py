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

def test_alternate_help_version():
    parser = test_argparse.ErrorRaisingArgumentParser()
    parser.add_argument('-x', action='help')
    parser.add_argument('-y', action='version')
    TestOptionalsHelpVersionActions.assertPrintHelpExit(parser, '-x')
    TestOptionalsHelpVersionActions.assertArgumentParserError(parser, '-v')
    TestOptionalsHelpVersionActions.assertArgumentParserError(parser, '--version')
    TestOptionalsHelpVersionActions.assertRaises(AttributeError, getattr, parser, 'format_version')

TestOptionalsHelpVersionActions = test_argparse.TestOptionalsHelpVersionActions()
test_alternate_help_version()

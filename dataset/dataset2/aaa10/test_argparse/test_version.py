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

def test_version():
    parser = test_argparse.ErrorRaisingArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='1.0')
    TestOptionalsHelpVersionActions.assertPrintHelpExit(parser, '-h')
    TestOptionalsHelpVersionActions.assertPrintHelpExit(parser, '--help')
    TestOptionalsHelpVersionActions.assertRaises(AttributeError, getattr, parser, 'format_version')

TestOptionalsHelpVersionActions = test_argparse.TestOptionalsHelpVersionActions()
test_version()

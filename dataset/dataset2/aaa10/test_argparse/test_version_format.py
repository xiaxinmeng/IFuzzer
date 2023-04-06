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

def test_version_format():
    parser = test_argparse.ErrorRaisingArgumentParser(prog='PPP')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 3.5')
    with TestOptionalsHelpVersionActions.assertRaises(test_argparse.ArgumentParserError) as cm:
        parser.parse_args(['-v'])
    TestOptionalsHelpVersionActions.assertEqual('PPP 3.5\n', cm.exception.stdout)

TestOptionalsHelpVersionActions = test_argparse.TestOptionalsHelpVersionActions()
test_version_format()

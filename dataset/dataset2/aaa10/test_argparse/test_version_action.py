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

def test_version_action():
    parser = test_argparse.ErrorRaisingArgumentParser(prog='XXX')
    parser.add_argument('-V', action='version', version='%(prog)s 3.7')
    with TestOptionalsHelpVersionActions.assertRaises(test_argparse.ArgumentParserError) as cm:
        parser.parse_args(['-V'])
    TestOptionalsHelpVersionActions.assertEqual('XXX 3.7\n', cm.exception.stdout)

TestOptionalsHelpVersionActions = test_argparse.TestOptionalsHelpVersionActions()
test_version_action()

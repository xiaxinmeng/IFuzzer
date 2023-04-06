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

def test_no_help():
    parser = test_argparse.ErrorRaisingArgumentParser(add_help=False)
    TestOptionalsHelpVersionActions.assertArgumentParserError(parser, '-h')
    TestOptionalsHelpVersionActions.assertArgumentParserError(parser, '--help')
    TestOptionalsHelpVersionActions.assertArgumentParserError(parser, '-v')
    TestOptionalsHelpVersionActions.assertArgumentParserError(parser, '--version')

TestOptionalsHelpVersionActions = test_argparse.TestOptionalsHelpVersionActions()
test_no_help()

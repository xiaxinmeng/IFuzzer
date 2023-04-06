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

def test_argument_type_error():

    def spam(string):
        raise argparse.ArgumentTypeError('spam!')
    parser = test_argparse.ErrorRaisingArgumentParser(prog='PROG', add_help=False)
    parser.add_argument('x', type=spam)
    with TestArgumentTypeError.assertRaises(test_argparse.ArgumentParserError) as cm:
        parser.parse_args(['XXX'])
    TestArgumentTypeError.assertEqual('usage: PROG x\nPROG: error: argument x: spam!\n', cm.exception.stderr)

TestArgumentTypeError = test_argparse.TestArgumentTypeError()
test_argument_type_error()

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

def test_optional_positional_not_in_message():
    parser = test_argparse.ErrorRaisingArgumentParser(prog='PROG', usage='')
    parser.add_argument('req_pos')
    parser.add_argument('optional_positional', nargs='?', default='eggs')
    with TestMessageContentError.assertRaises(test_argparse.ArgumentParserError) as cm:
        parser.parse_args([])
    msg = str(cm.exception)
    TestMessageContentError.assertRegex(msg, 'req_pos')
    TestMessageContentError.assertNotIn(msg, 'optional_positional')

TestMessageContentError = test_argparse.TestMessageContentError()
test_optional_positional_not_in_message()

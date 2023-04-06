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

def test_exclusive():
    parser = test_argparse.ErrorRaisingArgumentParser(prog='PROG')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--foo', action='store_true', help='FOO')
    group.add_argument('--spam', help='SPAM')
    parser.add_argument('badger', nargs='*', default='X', help='BADGER')
    args = parser.parse_intermixed_args('1 --foo 2'.split())
    TestIntermixedArgs.assertEqual(test_argparse.NS(badger=['1', '2'], foo=True, spam=None), args)
    TestIntermixedArgs.assertRaises(test_argparse.ArgumentParserError, parser.parse_intermixed_args, '1 2'.split())
    TestIntermixedArgs.assertEqual(group.required, True)

TestIntermixedArgs = test_argparse.TestIntermixedArgs()
test_exclusive()

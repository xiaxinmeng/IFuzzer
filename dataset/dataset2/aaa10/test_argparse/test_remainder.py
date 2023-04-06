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

def test_remainder():
    parser = test_argparse.ErrorRaisingArgumentParser(prog='PROG')
    parser.add_argument('-z')
    parser.add_argument('x')
    parser.add_argument('y', nargs='...')
    argv = 'X A B -z Z'.split()
    with TestIntermixedArgs.assertRaises(TypeError) as cm:
        parser.parse_intermixed_args(argv)
    TestIntermixedArgs.assertRegex(str(cm.exception), '\\.\\.\\.')

TestIntermixedArgs = test_argparse.TestIntermixedArgs()
test_remainder()

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

def test_optional_subparsers():
    parser = test_argparse.ErrorRaisingArgumentParser()
    subparsers = parser.add_subparsers(dest='command', required=False)
    subparsers.add_parser('run')
    ret = parser.parse_args(())
    TestAddSubparsers.assertIsNone(ret.command)

TestAddSubparsers = test_argparse.TestAddSubparsers()
test_optional_subparsers()

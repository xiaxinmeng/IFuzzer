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

def test_dest():
    parser = argparse.ArgumentParser()
    action = parser.add_argument('--foo')
    TestAddSubparsers.assertEqual(action.dest, 'foo')
    action = parser.add_argument('-b', '--bar')
    TestAddSubparsers.assertEqual(action.dest, 'bar')
    action = parser.add_argument('-x', '-y')
    TestAddSubparsers.assertEqual(action.dest, 'x')

TestAddSubparsers = test_argparse.TestAddSubparsers()
test_dest()

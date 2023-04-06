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

def test_misc():
    parser = argparse.ArgumentParser()
    action = parser.add_argument('--foo', nargs='?', const=42, default=84, type=int, choices=[1, 2], help='FOO', metavar='BAR', dest='baz')
    TestActionsReturned.assertEqual(action.nargs, '?')
    TestActionsReturned.assertEqual(action.const, 42)
    TestActionsReturned.assertEqual(action.default, 84)
    TestActionsReturned.assertEqual(action.type, int)
    TestActionsReturned.assertEqual(action.choices, [1, 2])
    TestActionsReturned.assertEqual(action.help, 'FOO')
    TestActionsReturned.assertEqual(action.metavar, 'BAR')
    TestActionsReturned.assertEqual(action.dest, 'baz')

TestActionsReturned = test_argparse.TestActionsReturned()
test_misc()

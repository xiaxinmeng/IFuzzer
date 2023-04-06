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

def test_optional():
    option = argparse.Action(option_strings=['--foo', '-a', '-b'], dest='b', type='int', nargs='+', default=42, choices=[1, 2, 3], help='HELP', metavar='METAVAR')
    string = "Action(option_strings=['--foo', '-a', '-b'], dest='b', nargs='+', const=None, default=42, type='int', choices=[1, 2, 3], help='HELP', metavar='METAVAR')"
    TestStrings.assertStringEqual(option, string)

TestStrings = test_argparse.TestStrings()
test_optional()

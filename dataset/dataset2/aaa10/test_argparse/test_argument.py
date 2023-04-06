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

def test_argument():
    argument = argparse.Action(option_strings=[], dest='x', type=float, nargs='?', default=2.5, choices=[0.5, 1.5, 2.5], help='H HH H', metavar='MV MV MV')
    string = "Action(option_strings=[], dest='x', nargs='?', const=None, default=2.5, type=%r, choices=[0.5, 1.5, 2.5], help='H HH H', metavar='MV MV MV')" % float
    TestStrings.assertStringEqual(argument, string)

TestStrings = test_argparse.TestStrings()
test_argument()

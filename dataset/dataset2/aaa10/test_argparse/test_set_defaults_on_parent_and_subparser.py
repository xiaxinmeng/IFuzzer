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

def test_set_defaults_on_parent_and_subparser():
    parser = argparse.ArgumentParser()
    xparser = parser.add_subparsers().add_parser('X')
    parser.set_defaults(foo=1)
    xparser.set_defaults(foo=2)
    TestSetDefaults.assertEqual(test_argparse.NS(foo=2), parser.parse_args(['X']))

TestSetDefaults = test_argparse.TestSetDefaults()
test_set_defaults_on_parent_and_subparser()

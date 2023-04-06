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

def test_set_defaults_parents():
    parent = test_argparse.ErrorRaisingArgumentParser(add_help=False)
    parent.set_defaults(x='foo')
    parser = test_argparse.ErrorRaisingArgumentParser(parents=[parent])
    TestSetDefaults.assertEqual(test_argparse.NS(x='foo'), parser.parse_args([]))

TestSetDefaults = test_argparse.TestSetDefaults()
test_set_defaults_parents()

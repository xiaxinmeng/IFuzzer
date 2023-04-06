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

def test_single_parent():
    parser = test_argparse.ErrorRaisingArgumentParser(parents=[TestParentParsers.wxyz_parent])
    TestParentParsers.assertEqual(parser.parse_args('-y 1 2 --w 3'.split()), test_argparse.NS(w='3', y='1', z='2'))

TestParentParsers = test_argparse.TestParentParsers()
TestParentParsers.setUp()
test_single_parent()

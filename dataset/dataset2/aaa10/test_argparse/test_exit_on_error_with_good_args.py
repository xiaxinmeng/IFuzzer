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

def test_exit_on_error_with_good_args():
    ns = TestExitOnError.parser.parse_args('--integers 4'.split())
    TestExitOnError.assertEqual(ns, argparse.Namespace(integers=4))

TestExitOnError = test_argparse.TestExitOnError()
TestExitOnError.setUp()
test_exit_on_error_with_good_args()

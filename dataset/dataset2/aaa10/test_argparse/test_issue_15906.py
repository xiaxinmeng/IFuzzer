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

def test_issue_15906():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', dest='test', type=str, default=[], action='append')
    args = parser.parse_args([])
    TestTypeFunctionCalledOnDefault.assertEqual(args.test, [])

TestTypeFunctionCalledOnDefault = test_argparse.TestTypeFunctionCalledOnDefault()
test_issue_15906()

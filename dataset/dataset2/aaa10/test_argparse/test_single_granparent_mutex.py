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

def test_single_granparent_mutex():
    parents = [TestParentParsers.ab_mutex_parent]
    parser = test_argparse.ErrorRaisingArgumentParser(add_help=False, parents=parents)
    parser = test_argparse.ErrorRaisingArgumentParser(parents=[parser])
    TestParentParsers._test_mutex_ab(parser.parse_args)

TestParentParsers = test_argparse.TestParentParsers()
TestParentParsers.setUp()
test_single_granparent_mutex()

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

def test_subparser1_help():
    TestAddSubparsers._test_subparser_help('5.0 1 -h', textwrap.dedent('            usage: PROG bar 1 [-h] [-w W] {a,b,c}\n\n            1 description\n\n            positional arguments:\n              {a,b,c}     x help\n\n            options:\n              -h, --help  show this help message and exit\n              -w W        w help\n            '))

TestAddSubparsers = test_argparse.TestAddSubparsers()
TestAddSubparsers.setUp()
test_subparser1_help()

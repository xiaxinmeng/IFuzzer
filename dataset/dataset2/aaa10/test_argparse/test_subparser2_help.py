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

def test_subparser2_help():
    TestAddSubparsers._test_subparser_help('5.0 2 -h', textwrap.dedent('            usage: PROG bar 2 [-h] [-y {1,2,3}] [z ...]\n\n            2 description\n\n            positional arguments:\n              z           z help\n\n            options:\n              -h, --help  show this help message and exit\n              -y {1,2,3}  y help\n            '))

TestAddSubparsers = test_argparse.TestAddSubparsers()
TestAddSubparsers.setUp()
test_subparser2_help()

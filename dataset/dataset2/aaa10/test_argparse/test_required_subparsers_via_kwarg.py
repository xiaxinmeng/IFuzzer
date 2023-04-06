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

def test_required_subparsers_via_kwarg():
    parser = test_argparse.ErrorRaisingArgumentParser()
    subparsers = parser.add_subparsers(dest='command', required=True)
    subparsers.add_parser('run')
    TestAddSubparsers._test_required_subparsers(parser)

TestAddSubparsers = test_argparse.TestAddSubparsers()
test_required_subparsers_via_kwarg()

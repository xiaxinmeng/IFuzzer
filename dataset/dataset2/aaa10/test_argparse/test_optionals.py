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

def test_optionals():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo')
    (args, extras) = parser.parse_known_args('--foo F --bar --baz'.split())
    TestParseKnownArgs.assertEqual(test_argparse.NS(foo='F'), args)
    TestParseKnownArgs.assertEqual(['--bar', '--baz'], extras)

TestParseKnownArgs = test_argparse.TestParseKnownArgs()
test_optionals()

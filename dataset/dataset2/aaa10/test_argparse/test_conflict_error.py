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

def test_conflict_error():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x')
    TestConflictHandling.assertRaises(argparse.ArgumentError, parser.add_argument, '-x')
    parser.add_argument('--spam')
    TestConflictHandling.assertRaises(argparse.ArgumentError, parser.add_argument, '--spam')

TestConflictHandling = test_argparse.TestConflictHandling()
test_conflict_error()

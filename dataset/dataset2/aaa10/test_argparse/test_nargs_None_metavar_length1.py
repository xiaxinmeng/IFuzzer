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

def test_nargs_None_metavar_length1():
    TestAddArgumentMetavar.do_test_no_exception(nargs=None, metavar=('1',))

TestAddArgumentMetavar = test_argparse.TestAddArgumentMetavar()
test_nargs_None_metavar_length1()

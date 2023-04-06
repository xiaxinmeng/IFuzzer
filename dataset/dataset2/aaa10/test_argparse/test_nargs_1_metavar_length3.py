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

def test_nargs_1_metavar_length3():
    TestAddArgumentMetavar.do_test_exception(nargs=1, metavar=('1', '2', '3'))

TestAddArgumentMetavar = test_argparse.TestAddArgumentMetavar()
test_nargs_1_metavar_length3()

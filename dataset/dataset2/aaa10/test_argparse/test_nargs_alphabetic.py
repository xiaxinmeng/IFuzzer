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

def test_nargs_alphabetic():
    TestInvalidNargs.do_test_invalid_exception(nargs='a')
    TestInvalidNargs.do_test_invalid_exception(nargs='abcd')

TestInvalidNargs = test_argparse.TestInvalidNargs()
test_nargs_alphabetic()

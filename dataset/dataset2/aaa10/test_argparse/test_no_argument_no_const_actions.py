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

def test_no_argument_no_const_actions():
    for action in ['store_true', 'store_false', 'count']:
        TestInvalidArgumentConstructors.assertTypeError('-x', const='foo', action=action)
        TestInvalidArgumentConstructors.assertTypeError('-x', nargs='*', action=action)

TestInvalidArgumentConstructors = test_argparse.TestInvalidArgumentConstructors()
test_no_argument_no_const_actions()

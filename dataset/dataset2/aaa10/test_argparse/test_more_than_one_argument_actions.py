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

def test_more_than_one_argument_actions():
    for action in ['store', 'append']:
        TestInvalidArgumentConstructors.assertValueError('-x', nargs=0, action=action)
        TestInvalidArgumentConstructors.assertValueError('spam', nargs=0, action=action)
        for nargs in [1, '*', '+']:
            TestInvalidArgumentConstructors.assertValueError('-x', const='foo', nargs=nargs, action=action)
            TestInvalidArgumentConstructors.assertValueError('spam', const='foo', nargs=nargs, action=action)

TestInvalidArgumentConstructors = test_argparse.TestInvalidArgumentConstructors()
test_more_than_one_argument_actions()

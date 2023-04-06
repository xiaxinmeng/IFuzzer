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

def test_invalid_action():
    TestInvalidArgumentConstructors.assertValueError('-x', action='foo')
    TestInvalidArgumentConstructors.assertValueError('foo', action='baz')
    TestInvalidArgumentConstructors.assertValueError('--foo', action=('store', 'append'))
    parser = argparse.ArgumentParser()
    with TestInvalidArgumentConstructors.assertRaises(ValueError) as cm:
        parser.add_argument('--foo', action='store-true')
    TestInvalidArgumentConstructors.assertIn('unknown action', str(cm.exception))

TestInvalidArgumentConstructors = test_argparse.TestInvalidArgumentConstructors()
test_invalid_action()

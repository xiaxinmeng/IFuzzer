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

def test_multiple_dest():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='foo')
    with TestInvalidArgumentConstructors.assertRaises(ValueError) as cm:
        parser.add_argument('bar', dest='baz')
    TestInvalidArgumentConstructors.assertIn('dest supplied twice for positional argument', str(cm.exception))

TestInvalidArgumentConstructors = test_argparse.TestInvalidArgumentConstructors()
test_multiple_dest()

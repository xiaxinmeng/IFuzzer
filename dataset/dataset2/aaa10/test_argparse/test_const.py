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

def test_const():
    parser = argparse.ArgumentParser()
    with TestBooleanOptionalAction.assertRaises(TypeError) as cm:
        parser.add_argument('--foo', const=True, action=argparse.BooleanOptionalAction)
    TestBooleanOptionalAction.assertIn("got an unexpected keyword argument 'const'", str(cm.exception))

TestBooleanOptionalAction = test_argparse.TestBooleanOptionalAction()
test_const()

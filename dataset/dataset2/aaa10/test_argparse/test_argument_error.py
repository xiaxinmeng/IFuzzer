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

def test_argument_error():
    msg = 'my error here'
    error = argparse.ArgumentError(None, msg)
    TestArgumentError.assertEqual(str(error), msg)

TestArgumentError = test_argparse.TestArgumentError()
test_argument_error()

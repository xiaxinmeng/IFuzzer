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

def test_missing_destination():
    TestInvalidArgumentConstructors.assertTypeError()
    for action in ['append', 'store']:
        TestInvalidArgumentConstructors.assertTypeError(action=action)

TestInvalidArgumentConstructors = test_argparse.TestInvalidArgumentConstructors()
test_missing_destination()

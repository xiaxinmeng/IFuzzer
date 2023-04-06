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

def test_no_argument_actions():
    for action in ['store_const', 'store_true', 'store_false', 'append_const', 'count']:
        for attrs in [dict(type=int), dict(nargs='+'), dict(choices='ab')]:
            TestInvalidArgumentConstructors.assertTypeError('-x', action=action, **attrs)

TestInvalidArgumentConstructors = test_argparse.TestInvalidArgumentConstructors()
test_no_argument_actions()

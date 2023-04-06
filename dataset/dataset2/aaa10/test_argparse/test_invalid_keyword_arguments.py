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

def test_invalid_keyword_arguments():
    TestInvalidArgumentConstructors.assertTypeError('-x', bar=None)
    TestInvalidArgumentConstructors.assertTypeError('-y', callback='foo')
    TestInvalidArgumentConstructors.assertTypeError('-y', callback_args=())
    TestInvalidArgumentConstructors.assertTypeError('-y', callback_kwargs={})

TestInvalidArgumentConstructors = test_argparse.TestInvalidArgumentConstructors()
test_invalid_keyword_arguments()

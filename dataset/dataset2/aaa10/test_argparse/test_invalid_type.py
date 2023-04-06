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

def test_invalid_type():
    TestInvalidArgumentConstructors.assertValueError('--foo', type='int')
    TestInvalidArgumentConstructors.assertValueError('--foo', type=(int, float))

TestInvalidArgumentConstructors = test_argparse.TestInvalidArgumentConstructors()
test_invalid_type()

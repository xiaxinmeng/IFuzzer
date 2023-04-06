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

def test_invalid_add_argument_group():
    parser = test_argparse.ErrorRaisingArgumentParser()
    raises = TestMutuallyExclusiveGroupErrors.assertRaises
    raises(TypeError, parser.add_mutually_exclusive_group, title='foo')

TestMutuallyExclusiveGroupErrors = test_argparse.TestMutuallyExclusiveGroupErrors()
test_invalid_add_argument_group()

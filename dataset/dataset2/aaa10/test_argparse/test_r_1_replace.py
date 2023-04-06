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

def test_r_1_replace():
    type = argparse.FileType('r', 1, errors='replace')
    TestFileTypeRepr.assertEqual("FileType('r', 1, errors='replace')", repr(type))

TestFileTypeRepr = test_argparse.TestFileTypeRepr()
test_r_1_replace()

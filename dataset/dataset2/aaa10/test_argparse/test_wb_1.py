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

def test_wb_1():
    type = argparse.FileType('wb', 1)
    TestFileTypeRepr.assertEqual("FileType('wb', 1)", repr(type))

TestFileTypeRepr = test_argparse.TestFileTypeRepr()
test_wb_1()

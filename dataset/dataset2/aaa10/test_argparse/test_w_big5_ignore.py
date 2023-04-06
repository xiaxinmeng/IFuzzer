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

def test_w_big5_ignore():
    type = argparse.FileType('w', encoding='big5', errors='ignore')
    TestFileTypeRepr.assertEqual("FileType('w', encoding='big5', errors='ignore')", repr(type))

TestFileTypeRepr = test_argparse.TestFileTypeRepr()
test_w_big5_ignore()

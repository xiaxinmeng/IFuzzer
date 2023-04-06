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

def test_r_latin():
    type = argparse.FileType('r', encoding='latin_1')
    TestFileTypeRepr.assertEqual("FileType('r', encoding='latin_1')", repr(type))

TestFileTypeRepr = test_argparse.TestFileTypeRepr()
test_r_latin()

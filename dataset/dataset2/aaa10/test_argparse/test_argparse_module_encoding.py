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

def test_argparse_module_encoding():
    TestEncoding._test_module_encoding(argparse.__file__)

TestEncoding = test_argparse.TestEncoding()
test_argparse_module_encoding()

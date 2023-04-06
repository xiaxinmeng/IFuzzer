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

def test_all_exports_everything_but_modules():
    items = [name for (name, value) in vars(argparse).items() if not (name.startswith('_') or name == 'ngettext') if not inspect.ismodule(value)]
    TestImportStar.assertEqual(sorted(items), sorted(argparse.__all__))

TestImportStar = test_argparse.TestImportStar()
test_all_exports_everything_but_modules()

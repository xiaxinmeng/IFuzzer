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

def test_format(AddTests, tester):
    parser = AddTests._get_parser(tester)
    format = getattr(parser, 'format_%s' % AddTests.func_suffix)
    AddTests._test(tester, format())

AddTests = test_argparse.AddTests()
test_format()

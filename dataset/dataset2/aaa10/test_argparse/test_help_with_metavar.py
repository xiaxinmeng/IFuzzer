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

def test_help_with_metavar():
    help_text = TestWrappingMetavar.parser.format_help()
    TestWrappingMetavar.assertEqual(help_text, textwrap.dedent('            usage: this_is_spammy_prog_with_a_long_name_sorry_about_the_name\n                   [-h] [--proxy <http[s]://example:1234>]\n\n            options:\n              -h, --help            show this help message and exit\n              --proxy <http[s]://example:1234>\n            '))

TestWrappingMetavar = test_argparse.TestWrappingMetavar()
TestWrappingMetavar.setUp()
test_help_with_metavar()

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

def test_successes_when_required():
    parse_args = MEMixin.get_parser(required=True).parse_args
    for (args_string, expected_ns) in MEMixin.successes:
        actual_ns = parse_args(args_string.split())
        MEMixin.assertEqual(actual_ns, expected_ns)

MEMixin = test_argparse.MEMixin()
test_successes_when_required()

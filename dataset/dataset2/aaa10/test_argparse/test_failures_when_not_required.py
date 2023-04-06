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

def test_failures_when_not_required():
    parse_args = MEMixin.get_parser(required=False).parse_args
    error = ArgumentParserError
    for args_string in MEMixin.failures:
        MEMixin.assertRaises(error, parse_args, args_string.split())

MEMixin = test_argparse.MEMixin()
test_failures_when_not_required()

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

def test_type_function_call_only_once():

    def spam(string_to_convert):
        TestTypeFunctionCallOnlyOnce.assertEqual(string_to_convert, 'spam!')
        return 'foo_converted'
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', type=spam, default='bar')
    args = parser.parse_args('--foo spam!'.split())
    TestTypeFunctionCallOnlyOnce.assertEqual(test_argparse.NS(foo='foo_converted'), args)

TestTypeFunctionCallOnlyOnce = test_argparse.TestTypeFunctionCallOnlyOnce()
test_type_function_call_only_once()

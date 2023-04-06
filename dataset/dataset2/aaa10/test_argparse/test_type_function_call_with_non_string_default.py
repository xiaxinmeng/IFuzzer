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

def test_type_function_call_with_non_string_default():

    def spam(int_to_convert):
        TestTypeFunctionCalledOnDefault.assertEqual(int_to_convert, 0)
        return 'foo_converted'
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', type=spam, default=0)
    args = parser.parse_args([])
    TestTypeFunctionCalledOnDefault.assertEqual(test_argparse.NS(foo=0), args)

TestTypeFunctionCalledOnDefault = test_argparse.TestTypeFunctionCalledOnDefault()
test_type_function_call_with_non_string_default()

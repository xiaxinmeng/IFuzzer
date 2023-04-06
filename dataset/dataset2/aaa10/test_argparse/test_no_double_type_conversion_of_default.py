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

def test_no_double_type_conversion_of_default():

    def extend(str_to_convert):
        return str_to_convert + '*'
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', type=extend, default='*')
    args = parser.parse_args([])
    TestTypeFunctionCalledOnDefault.assertEqual(test_argparse.NS(test='**'), args)

TestTypeFunctionCalledOnDefault = test_argparse.TestTypeFunctionCalledOnDefault()
test_no_double_type_conversion_of_default()

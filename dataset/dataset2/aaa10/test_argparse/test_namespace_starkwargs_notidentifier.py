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

def test_namespace_starkwargs_notidentifier():
    ns = argparse.Namespace(**{'"': 'quote'})
    string = 'Namespace(**{\'"\': \'quote\'})'
    TestStrings.assertStringEqual(ns, string)

TestStrings = test_argparse.TestStrings()
test_namespace_starkwargs_notidentifier()

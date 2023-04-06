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

def test_namespace():
    ns = argparse.Namespace(foo=42, bar='spam')
    string = "Namespace(foo=42, bar='spam')"
    TestStrings.assertStringEqual(ns, string)

TestStrings = test_argparse.TestStrings()
test_namespace()

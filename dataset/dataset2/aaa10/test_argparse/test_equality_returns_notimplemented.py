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

def test_equality_returns_notimplemented():
    ns = argparse.Namespace(a=1, b=2)
    TestNamespace.assertIs(ns.__eq__(None), NotImplemented)
    TestNamespace.assertIs(ns.__ne__(None), NotImplemented)

TestNamespace = test_argparse.TestNamespace()
test_equality_returns_notimplemented()

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

def test_constructor():
    ns = argparse.Namespace()
    TestNamespace.assertRaises(AttributeError, getattr, ns, 'x')
    ns = argparse.Namespace(a=42, b='spam')
    TestNamespace.assertEqual(ns.a, 42)
    TestNamespace.assertEqual(ns.b, 'spam')

TestNamespace = test_argparse.TestNamespace()
test_constructor()

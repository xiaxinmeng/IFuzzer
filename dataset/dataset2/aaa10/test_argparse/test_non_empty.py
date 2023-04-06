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

def test_non_empty():
    ns = argparse.Namespace(x=1, y=2)
    TestNamespaceContainsSimple.assertNotIn('', ns)
    TestNamespaceContainsSimple.assertIn('x', ns)
    TestNamespaceContainsSimple.assertIn('y', ns)
    TestNamespaceContainsSimple.assertNotIn('xx', ns)
    TestNamespaceContainsSimple.assertNotIn('z', ns)

TestNamespaceContainsSimple = test_argparse.TestNamespaceContainsSimple()
test_non_empty()

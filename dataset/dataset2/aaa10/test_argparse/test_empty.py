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

def test_empty():
    ns = argparse.Namespace()
    TestNamespaceContainsSimple.assertNotIn('', ns)
    TestNamespaceContainsSimple.assertNotIn('x', ns)

TestNamespaceContainsSimple = test_argparse.TestNamespaceContainsSimple()
test_empty()

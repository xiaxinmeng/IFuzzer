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

def test_bad_type():
    TestConflictHandling.assertRaises(ValueError, argparse.ArgumentParser, conflict_handler='foo')

TestConflictHandling = test_argparse.TestConflictHandling()
test_bad_type()

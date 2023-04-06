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

def test_conflicting_parents_mutex():
    TestParentParsers.assertRaises(argparse.ArgumentError, argparse.ArgumentParser, parents=[TestParentParsers.abcd_parent, TestParentParsers.ab_mutex_parent])

TestParentParsers = test_argparse.TestParentParsers()
TestParentParsers.setUp()
test_conflicting_parents_mutex()

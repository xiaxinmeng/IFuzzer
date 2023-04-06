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

def test_wrapper(AddTests, test_func=test_argparse.test_func):
    test_func(AddTests)

AddTests = test_argparse.AddTests()
test_wrapper()

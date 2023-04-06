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

def test_parser():
    parser = argparse.ArgumentParser(prog='PROG')
    string = "ArgumentParser(prog='PROG', usage=None, description=None, formatter_class=%r, conflict_handler='error', add_help=True)" % argparse.HelpFormatter
    TestStrings.assertStringEqual(parser, string)

TestStrings = test_argparse.TestStrings()
test_parser()

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

def test_arguments_list_positional():
    parser = argparse.ArgumentParser()
    parser.add_argument('x')
    parser.parse_args(['x'])

TestParseKnownArgs = test_argparse.TestParseKnownArgs()
test_arguments_list_positional()

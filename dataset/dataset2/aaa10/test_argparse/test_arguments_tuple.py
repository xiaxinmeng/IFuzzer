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

def test_arguments_tuple():
    parser = argparse.ArgumentParser()
    parser.parse_args(())

TestParseKnownArgs = test_argparse.TestParseKnownArgs()
test_arguments_tuple()

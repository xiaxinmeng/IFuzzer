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

def test_parsers_action_missing_params():
    TestInvalidArgumentConstructors.assertTypeError('command', action='parsers')
    TestInvalidArgumentConstructors.assertTypeError('command', action='parsers', prog='PROG')
    TestInvalidArgumentConstructors.assertTypeError('command', action='parsers', parser_class=argparse.ArgumentParser)

TestInvalidArgumentConstructors = test_argparse.TestInvalidArgumentConstructors()
test_parsers_action_missing_params()

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

def test_usage_when_not_required():
    format_usage = MEMixin.get_parser(required=False).format_usage
    expected_usage = MEMixin.usage_when_not_required
    MEMixin.assertEqual(format_usage(), textwrap.dedent(expected_usage))

MEMixin = test_argparse.MEMixin()
test_usage_when_not_required()

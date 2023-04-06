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

def test_help_when_not_required():
    format_help = MEMixin.get_parser(required=False).format_help
    help = MEMixin.usage_when_not_required + MEMixin.help
    MEMixin.assertEqual(format_help(), textwrap.dedent(help))

MEMixin = test_argparse.MEMixin()
test_help_when_not_required()

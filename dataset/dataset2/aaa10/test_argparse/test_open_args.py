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

def test_open_args():
    FT = argparse.FileType
    cases = [(FT('rb'), ('rb', -1, None, None)), (FT('w', 1), ('w', 1, None, None)), (FT('w', errors='replace'), ('w', -1, None, 'replace')), (FT('wb', encoding='big5'), ('wb', -1, 'big5', None)), (FT('w', 0, 'l1', 'strict'), ('w', 0, 'l1', 'strict'))]
    with mock.patch('builtins.open') as m:
        for (type, args) in cases:
            type('foo')
            m.assert_called_with('foo', *args)

TestFileTypeOpenArgs = test_argparse.TestFileTypeOpenArgs()
test_open_args()

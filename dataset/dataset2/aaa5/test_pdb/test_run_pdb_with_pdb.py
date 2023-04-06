import doctest
import os
import pdb
import sys
import types
import codecs
import unittest
import subprocess
import textwrap
from contextlib import ExitStack
from io import StringIO
from test.support import os_helper
from test.test_doctest import _FakeInput
from unittest.mock import patch
from test import test_pdb
import test_pdb

def test_run_pdb_with_pdb():
    commands = '\n            c\n            quit\n        '
    (stdout, stderr) = PdbTestCase._run_pdb(['-m', 'pdb'], commands)
    PdbTestCase.assertIn(pdb._usage, stdout.replace('\r', ''))

PdbTestCase = test_pdb.PdbTestCase()
test_run_pdb_with_pdb()

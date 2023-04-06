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

def test_issue7964():
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(b'print("testing my pdb")\r\n')
    cmd = [sys.executable, '-m', 'pdb', os_helper.TESTFN]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    PdbTestCase.addCleanup(proc.stdout.close)
    (stdout, stderr) = proc.communicate(b'quit\n')
    PdbTestCase.assertNotIn(b'SyntaxError', stdout, 'Got a syntax error running test script under PDB')

PdbTestCase = test_pdb.PdbTestCase()
test_issue7964()

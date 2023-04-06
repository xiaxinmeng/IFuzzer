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

def test_header():
    stdout = StringIO()
    header = 'Nobody expects... blah, blah, blah'
    with ExitStack() as resources:
        resources.enter_context(patch('sys.stdout', stdout))
        resources.enter_context(patch.object(pdb.Pdb, 'set_trace'))
        pdb.set_trace(header=header)
    PdbTestCase.assertEqual(stdout.getvalue(), header + '\n')

PdbTestCase = test_pdb.PdbTestCase()
test_header()

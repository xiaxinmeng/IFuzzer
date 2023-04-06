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

def test_errors_in_command():
    commands = '\n'.join(['print(', 'debug print(', 'debug doesnotexist', 'c'])
    (stdout, _) = PdbTestCase.run_pdb_script('pass', commands + '\n')
    PdbTestCase.assertEqual(stdout.splitlines()[1:], ['-> pass', '(Pdb) *** SyntaxError: unexpected EOF while parsing', '(Pdb) ENTERING RECURSIVE DEBUGGER', '*** SyntaxError: unexpected EOF while parsing', 'LEAVING RECURSIVE DEBUGGER', '(Pdb) ENTERING RECURSIVE DEBUGGER', '> <string>(1)<module>()', "((Pdb)) *** NameError: name 'doesnotexist' is not defined", 'LEAVING RECURSIVE DEBUGGER', '(Pdb) '])

PdbTestCase = test_pdb.PdbTestCase()
test_errors_in_command()

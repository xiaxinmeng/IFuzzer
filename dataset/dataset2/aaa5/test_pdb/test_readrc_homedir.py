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

def test_readrc_homedir():
    save_home = os.environ.pop('HOME', None)
    with os_helper.temp_dir() as temp_dir, patch('os.path.expanduser'):
        rc_path = os.path.join(temp_dir, '.pdbrc')
        os.path.expanduser.return_value = rc_path
        try:
            with open(rc_path, 'w') as f:
                f.write('invalid')
            PdbTestCase.assertEqual(pdb.Pdb().rcLines[0], 'invalid')
        finally:
            if save_home is not None:
                os.environ['HOME'] = save_home

PdbTestCase = test_pdb.PdbTestCase()
test_readrc_homedir()

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

def test_issue36250():
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(textwrap.dedent('\n                import threading\n                import pdb\n\n                evt = threading.Event()\n\n                def start_pdb():\n                    evt.wait()\n                    pdb.Pdb(readrc=False).set_trace()\n\n                t = threading.Thread(target=start_pdb)\n                t.start()\n                pdb.Pdb(readrc=False).set_trace()\n                evt.set()\n                t.join()').encode('ascii'))
    cmd = [sys.executable, '-u', os_helper.TESTFN]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, env={**os.environ, 'PYTHONIOENCODING': 'utf-8'})
    PdbTestCase.addCleanup(proc.stdout.close)
    (stdout, stderr) = proc.communicate(b'cont\ncont\n')
    PdbTestCase.assertNotIn(b'Error', stdout, 'Got an error running test script under PDB')

PdbTestCase = test_pdb.PdbTestCase()
test_issue36250()

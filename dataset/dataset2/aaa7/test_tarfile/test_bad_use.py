import sys
import os
import io
from hashlib import sha256
from contextlib import contextmanager
from random import Random
import pathlib
import unittest
import unittest.mock
import tarfile
from test import support
from test.support import os_helper
from test.support import script_helper
import gzip

import pwd, grp
import test_tarfile

def test_bad_use():
    (rc, out, err) = CommandLineTest.tarfilecmd_failure()
    CommandLineTest.assertEqual(out, b'')
    CommandLineTest.assertIn(b'usage', err.lower())
    CommandLineTest.assertIn(b'error', err.lower())
    CommandLineTest.assertIn(b'required', err.lower())
    (rc, out, err) = CommandLineTest.tarfilecmd_failure('-l', '')
    CommandLineTest.assertEqual(out, b'')
    CommandLineTest.assertNotEqual(err.strip(), b'')

CommandLineTest = test_tarfile.CommandLineTest()
test_bad_use()

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

def test_extract_command():
    CommandLineTest.make_simple_tarfile(test_tarfile.tmpname)
    for opt in ('-e', '--extract'):
        try:
            with os_helper.temp_cwd(tarextdir):
                out = CommandLineTest.tarfilecmd(opt, tmpname)
            CommandLineTest.assertEqual(out, b'')
        finally:
            os_helper.rmtree(tarextdir)

CommandLineTest = test_tarfile.CommandLineTest()
test_extract_command()

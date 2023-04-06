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

def test_create_command():
    files = [support.findfile('tokenize_tests.txt'), support.findfile('tokenize_tests-no-coding-cookie-and-utf8-bom-sig-only.txt')]
    for opt in ('-c', '--create'):
        try:
            out = CommandLineTest.tarfilecmd(opt, test_tarfile.tmpname, *files)
            CommandLineTest.assertEqual(out, b'')
            with tarfile.open(test_tarfile.tmpname) as tar:
                tar.getmembers()
        finally:
            os_helper.unlink(test_tarfile.tmpname)

CommandLineTest = test_tarfile.CommandLineTest()
test_create_command()

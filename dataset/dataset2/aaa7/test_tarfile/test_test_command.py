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

def test_test_command():
    for tar_name in test_tarfile.testtarnames:
        for opt in ('-t', '--test'):
            out = CommandLineTest.tarfilecmd(opt, tar_name)
            CommandLineTest.assertEqual(out, b'')

CommandLineTest = test_tarfile.CommandLineTest()
CommandLineTest.setUp()
test_test_command()

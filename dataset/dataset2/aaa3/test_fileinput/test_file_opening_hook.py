import os
import sys
import re
import fileinput
import collections
import builtins
import tempfile
import unittest

import gzip
from io import BytesIO, StringIO
from fileinput import FileInput, hook_encoded
from pathlib import Path
from test.support import verbose
from test.support.os_helper import TESTFN
from test.support.os_helper import unlink as safe_unlink
from test.support import os_helper
from test.support import warnings_helper
from test import support
from unittest import mock
import test_fileinput

def test_file_opening_hook():
    try:
        fi = FileInput(inplace=1, openhook=lambda f, m: None)
        FileInputTests.fail('FileInput should raise if both inplace and openhook arguments are given')
    except ValueError:
        pass
    try:
        fi = FileInput(openhook=1)
        FileInputTests.fail('FileInput should check openhook for being callable')
    except ValueError:
        pass

    class CustomOpenHook:

        def __init__(FileInputTests):
            FileInputTests.invoked = False

        def __call__(FileInputTests, *args):
            FileInputTests.invoked = True
            return open(*args)
    t = FileInputTests.writeTmp('\n')
    custom_open_hook = CustomOpenHook()
    with FileInput([t], openhook=custom_open_hook) as fi:
        fi.readline()
    FileInputTests.assertTrue(custom_open_hook.invoked, 'openhook not invoked')

FileInputTests = test_fileinput.FileInputTests()
test_file_opening_hook()

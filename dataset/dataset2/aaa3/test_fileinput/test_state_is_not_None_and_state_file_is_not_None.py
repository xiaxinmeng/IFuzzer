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

def test_state_is_not_None_and_state_file_is_not_None():
    """Tests invoking fileinput.input() when fileinput._state is not None
           and its _file attribute is also not None.  Expect RuntimeError to
           be raised with a meaningful error message and for fileinput._state
           to *not* be modified."""
    instance = test_fileinput.MockFileInput()
    instance._file = object()
    fileinput._state = instance
    with Test_fileinput_input.assertRaises(RuntimeError) as cm:
        fileinput.input()
    Test_fileinput_input.assertEqual(('input() already active',), cm.exception.args)
    Test_fileinput_input.assertIs(instance, fileinput._state, 'fileinput._state')

Test_fileinput_input = test_fileinput.Test_fileinput_input()
Test_fileinput_input.setUp()
test_state_is_not_None_and_state_file_is_not_None()
